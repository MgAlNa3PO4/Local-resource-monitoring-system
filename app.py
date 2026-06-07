#!/usr/bin/env python3
"""
本机资源监控网站 - Flask 后端
支持：CPU、内存、磁盘、网络、进程 实时监控
可在局域网内任意设备访问
"""

import os
import time
import json
import platform
import subprocess
from functools import lru_cache
from datetime import datetime

import psutil
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# ============================================================
# 辅助函数
# ============================================================

def get_size(bytes):
    """将字节转换为人类可读格式"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} PB"


def get_uptime():
    """获取系统运行时间"""
    uptime_seconds = time.time() - psutil.boot_time()
    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    return f"{days}天 {hours}小时 {minutes}分钟"


def get_network_io():
    """获取网络IO速率（需要采样两次）"""
    net1 = psutil.net_io_counters()
    time.sleep(0.5)
    net2 = psutil.net_io_counters()

    delta_time = 0.5
    sent_speed = (net2.bytes_sent - net1.bytes_sent) / delta_time
    recv_speed = (net2.bytes_recv - net1.bytes_recv) / delta_time
    return sent_speed, recv_speed


def get_cpu_temp():
    """获取 CPU 温度（Linux 特有）"""
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            return temps['coretemp'][0].current
        elif 'k10temp' in temps:
            return temps['k10temp'][0].current
        elif 'cpu-thermal' in temps:
            return temps['cpu-thermal'][0].current
        elif 'acpitz' in temps:
            return temps['acpitz'][0].current
    except Exception:
        pass
    return None


def get_process_list(sort_by='cpu', limit=20):
    """获取进程列表"""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent',
                                      'memory_info', 'status', 'create_time',
                                      'username', 'num_threads']):
        try:
            pinfo = proc.info
            pinfo['memory_mb'] = pinfo['memory_info'].rss / 1024 / 1024 if pinfo['memory_info'] else 0
            processes.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if sort_by == 'cpu':
        processes.sort(key=lambda p: p.get('cpu_percent', 0) or 0, reverse=True)
    elif sort_by == 'memory':
        processes.sort(key=lambda p: p.get('memory_mb', 0) or 0, reverse=True)

    return processes[:limit]


# ============================================================
# API 路由
# ============================================================

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/overview')
def api_overview():
    """概览数据：CPU、内存、磁盘、网络、系统信息"""
    cpu_percent = psutil.cpu_percent(interval=0.3)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()

    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    disk = psutil.disk_usage('/')
    disk_partitions = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disk_partitions.append({
                'device': part.device,
                'mountpoint': part.mountpoint,
                'fstype': part.fstype,
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            })
        except (PermissionError, OSError):
            pass

    sent_speed, recv_speed = get_network_io()
    net = psutil.net_io_counters()

    cpu_temp = get_cpu_temp()

    return jsonify({
        'hostname': platform.node(),
        'platform': f"{platform.system()} {platform.release()}",
        'uptime': get_uptime(),
        'boot_time': psutil.boot_time(),
        'cpu': {
            'percent': cpu_percent,
            'count': cpu_count,
            'physical_count': psutil.cpu_count(logical=False),
            'freq_current': cpu_freq.current if cpu_freq else 0,
            'freq_max': cpu_freq.max if cpu_freq else 0,
            'temperature': cpu_temp,
            'load_avg': [round(x, 2) for x in os.getloadavg()] if hasattr(os, 'getloadavg') else []
        },
        'memory': {
            'total': memory.total,
            'available': memory.available,
            'used': memory.used,
            'percent': memory.percent,
            'swap_total': swap.total,
            'swap_used': swap.used,
            'swap_percent': swap.percent
        },
        'disk': {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        },
        'disk_partitions': disk_partitions,
        'network': {
            'bytes_sent': net.bytes_sent,
            'bytes_recv': net.bytes_recv,
            'packets_sent': net.packets_sent,
            'packets_recv': net.packets_recv,
            'speed_sent': sent_speed,
            'speed_recv': recv_speed
        },
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })


@app.route('/api/cpu_history')
def api_cpu_history():
    """返回 CPU 历史数据（最近60秒）"""
    seconds = min(int(request.args.get('seconds', 60)), 300)
    data = []
    for _ in range(min(seconds, 60)):
        data.append(psutil.cpu_percent(interval=1))
    return jsonify({
        'data': data,
        'label': list(range(-len(data), 0))
    })


@app.route('/api/processes')
def api_processes():
    """进程列表"""
    sort_by = request.args.get('sort', 'cpu')
    limit = min(int(request.args.get('limit', 20)), 100)
    return jsonify({
        'processes': [{
            'pid': p['pid'],
            'name': p['name'],
            'cpu': p.get('cpu_percent', 0) or 0,
            'memory': round(p.get('memory_mb', 0) or 0, 1),
            'status': p.get('status', ''),
            'threads': p.get('num_threads', 0),
            'user': p.get('username', ''),
            'created': datetime.fromtimestamp(p.get('create_time', 0)).strftime('%H:%M:%S')
            if p.get('create_time') else ''
        } for p in get_process_list(sort_by, limit)]
    })


@app.route('/api/disks')
def api_disks():
    """所有磁盘分区详情"""
    partitions = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            partitions.append({
                'device': part.device,
                'mountpoint': part.mountpoint,
                'fstype': part.fstype,
                'total': get_size(usage.total),
                'used': get_size(usage.used),
                'free': get_size(usage.free),
                'percent': usage.percent
            })
        except (PermissionError, OSError):
            pass
    return jsonify({'partitions': partitions})


@app.route('/api/network')
def api_network():
    """网络接口详情"""
    interfaces = []
    for name, addrs in psutil.net_if_addrs().items():
        ipv4 = next((a.address for a in addrs if a.family == 2), None)  # AF_INET
        mac = next((a.address for a in addrs if a.family == 17), None)  # AF_PACKET
        interfaces.append({
            'name': name,
            'ip': ipv4,
            'mac': mac
        })
    return jsonify({'interfaces': interfaces})


if __name__ == '__main__':
    # 监听 0.0.0.0 允许局域网访问
    # 默认端口 5000，可通过环境变量 PORT 修改
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 资源监控系统启动！")
    print(f"   本机访问: http://127.0.0.1:{port}")
    # 获取本机局域网IP
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '无法获取'
    finally:
        s.close()
    print(f"   局域网访问: http://{local_ip}:{port}")
    print(f"   按 Ctrl+C 停止服务")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
