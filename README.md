<div align="center">

# 📊 Local Resource Monitoring System

**基于 Python Flask + Chart.js 的轻量级本机资源监控仪表盘**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=flat&logo=chartdotjs&logoColor=white)](https://www.chartjs.org)
[![psutil](https://img.shields.io/badge/psutil-7.2-0A8C5C?style=flat)](https://github.com/giampaolo/psutil)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-232F3E?style=flat)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat)]()

**无需安装任何 Agent 或复杂工具，一条命令启动，浏览器打开即用！**

</div>

---

## 📋 目录

- [✨ 功能特性](#-功能特性)
- [🖥️ 界面预览](#️-界面预览)
- [🚀 快速开始](#-快速开始)
- [📡 局域网访问](#-局域网访问)
- [🔧 API 文档](#-api-文档)
- [📁 项目结构](#-项目结构)
- [⚙️ 自定义配置](#️-自定义配置)
- [🛠️ 技术栈](#️-技术栈)
- [❓ 常见问题](#-常见问题)
- [📄 开源协议](#-开源协议)

---

## ✨ 功能特性

| 特性 | 说明 |
|------|------|
| ⚡ **CPU 实时监控** | 使用率、逻辑/物理核心数、实时频率、负载均值、CPU 温度 |
| 🧠 **内存监控** | 物理内存使用率、已用/可用/总量、Swap 交换分区 |
| 💾 **磁盘监控** | 根分区及所有挂载点的使用率、已用/剩余空间、文件系统类型 |
| 🌐 **网络监控** | 实时上传/下载速率、总收发字节数、各网络接口 IP 与 MAC |
| 📈 **历史趋势图** | CPU & 内存 60 秒动态曲线，网页上就能看到变化趋势 |
| ⚙️ **进程 TOP 20** | 按 CPU 或内存排序，一键切换排序方式 |
| 📡 **局域网访问** | 同一网络下的手机、平板、其他电脑均可实时查看 |
| 🔄 **自动刷新** | 每 2 秒自动拉取最新数据，无需手动刷新页面 |

---

## 🖥️ 界面预览

```
┌─────────────────────────────────────────────────────────────┐
│  📊 本机资源监控                       运行时长: 3天2小时 ● │
├──────────┬──────────┬──────────┬────────────────────────────┤
│ ⚡ CPU    │ 🧠 内存  │ 💾 磁盘  │ 🌐 网络                    │
│  12.5%   │  45.2%   │  3.3%   │ ↑ 1.2 MB/s                 │
│ 8核/16逻辑│ 8.0/16GB │ 32/1TB  │ ↓ 3.5 MB/s                 │
├──────────┴──────────┴──────────┴────────────────────────────┤
│ 📈 CPU & 内存历史趋势图 (最近60秒)                           │
│  ▁▂▃▄▅▆▇█▇▆▅▄▃▂▁  CPU  ▁▂▃▄▅▆▇█▇▆▅▄▃▂▁  内存               │
├──────────────────────┬─────────────────────────────────────┤
│ 🖥️ 系统信息           │ 📁 磁盘分区                         │
│ 主机名: my-pc        │ /        ████░░░░  3.3%  32G/1TB   │
│ 系统: Ubuntu 24.04   │ /mnt/d   ██████░░  55.0%   ●        │
│ CPU: Intel i7-13700H │ /mnt/e   ██░░░░░░  15.2%            │
│ 温度: 52°C          │                                       │
├──────────────────────┴─────────────────────────────────────┤
│ ⚙️ 进程 TOP 20 (按 CPU ▼)                                   │
│ PID  │ 名称              │ CPU %  │ 内存 MB  │ 线程 │ 状态 │
│ ─────┼───────────────────┼────────┼─────────┼──────┼──────│
│ 1234 │ python3           │  45.2  │  256.0  │ 4    │ run  │
│ 5678 │ chrome            │  12.1  │  1024.0 │ 16   │ run  │
│ ...                                                     │
└─────────────────────────────────────────────────────────────┘
```

> 💡 深色主题，视觉友好，所有设备上的浏览体验一致。

---

## 🚀 快速开始

### 环境要求

| 依赖 | 最低版本 |
|------|---------|
| Python | 3.8+ |
| pip | 20.0+ |
| 操作系统 | Linux / macOS / Windows (WSL 均可) |

### 安装 & 运行

**方式一：从 GitHub 克隆（推荐）**

```bash
# 1. 克隆仓库
git clone https://github.com/MgAlNa3PO4/Local-resource-monitoring-system.git
cd Local-resource-monitoring-system

# 2. 创建虚拟环境并安装依赖
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows

pip install -r requirements.txt

# 3. 启动服务
python app.py
```

**方式二：直接下载文件**

```bash
# 1. 创建项目目录
mkdir resource-monitor && cd resource-monitor

# 2. 下载程序文件
#    从 https://github.com/MgAlNa3PO4/Local-resource-monitoring-system 下载 app.py 和 templates/index.html

# 3. 创建虚拟环境并安装依赖
python3 -m venv venv
source venv/bin/activate
pip install flask psutil

# 4. 启动服务
python app.py
```

### 验证是否启动成功

启动后终端会显示：

```
🚀 资源监控系统启动！
   本机访问: http://127.0.0.1:5000
   局域网访问: http://172.21.145.73:5000
   按 Ctrl+C 停止服务
```

> ✅ 用浏览器打开显示仪表盘即表示成功！

---

## 📡 局域网访问

在同一局域网（WiFi / 有线）下，用手机、平板或其他电脑打开：

```
http://你的电脑局域网IP:5000
```

**如何查看你的局域网 IP？**

| 系统 | 命令 |
|------|------|
| Linux / WSL | `hostname -I` 或 `ip addr` |
| macOS | `ifconfig \| grep inet` |
| Windows | `ipconfig`（找 IPv4 地址） |

> ⚠️ 确保防火墙没有阻止 5000 端口

---

## 🔧 API 文档

本项目提供 RESTful API，方便二次开发或集成到其他系统。

### 概览接口

```
GET /api/overview
```

返回 CPU、内存、磁盘、网络、系统信息的完整快照。

**响应示例：**

```json
{
  "hostname": "my-pc",
  "platform": "Linux 6.8.0",
  "uptime": "3天 2小时 15分钟",
  "cpu": {
    "percent": 12.5,
    "count": 16,
    "physical_count": 8,
    "freq_current": 3600.0,
    "temperature": 52.3,
    "load_avg": [0.5, 0.3, 0.1]
  },
  "memory": {
    "total": 17179869184,
    "available": 9412853760,
    "used": 7767015424,
    "percent": 45.2,
    "swap_total": 8589934592,
    "swap_used": 1048576000,
    "swap_percent": 12.2
  },
  "disk": {
    "total": 1081101176832,
    "used": 34102759424,
    "free": 992006062080,
    "percent": 3.3
  },
  "network": {
    "bytes_sent": 1234567890,
    "bytes_recv": 9876543210,
    "speed_sent": 1250000.0,
    "speed_recv": 3500000.0
  }
}
```

### CPU 历史数据

```
GET /api/cpu_history?seconds=60
```

返回最近 N 秒（默认 60，最大 300）的 CPU 使用率采样数据。

### 进程列表

```
GET /api/processes?sort=cpu&limit=20
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `sort` | 排序方式：`cpu` 或 `memory` | `cpu` |
| `limit` | 返回条数（最大 100） | `20` |

### 磁盘分区

```
GET /api/disks
```

返回所有磁盘分区的详细信息，包括挂载点、设备名、文件系统类型、使用率等。

### 网络接口

```
GET /api/network
```

返回各网络接口的名称、IP 地址、MAC 地址。

---

## 📁 项目结构

```
Local-resource-monitoring-system/
├── app.py                    # 🎯 Flask 后端主程序（所有 API + 路由）
├── templates/
│   └── index.html            # 🎨 前端仪表盘页面（Chart.js + 自动刷新）
├── static/                   # 📦 静态资源目录（预留）
├── requirements.txt          # 📋 Python 依赖清单
├── README.md                 # 📖 项目文档
└── .gitignore                # 🙈 Git 忽略规则
```

**核心文件说明：**

| 文件 | 职责 |
|------|------|
| `app.py` | 后端逻辑 + API 接口，使用 `psutil` 采集系统数据，Flask 提供 HTTP 服务 |
| `templates/index.html` | 单页面应用，使用 Chart.js 绘制图表，每 2 秒自动拉取数据刷新 |
| `requirements.txt` | 仅需 `flask` 和 `psutil` 两个依赖，极致轻量 |

---

## ⚙️ 自定义配置

### 修改端口

```bash
PORT=8080 python app.py
```

### 修改刷新频率

编辑 `templates/index.html`，找到 `const INTERVAL = 2000;`（默认 2 秒），改为你想要的毫秒数：

```javascript
const INTERVAL = 5000;  // 改为 5 秒刷新一次
```

### 修改进程显示数量

编辑 `templates/index.html`，找到 `fetchProcesses()` 函数中的 `sort&limit=20` 改为你想要的数字：

```javascript
const res = await fetch(`/api/processes?sort=${currentSort}&limit=50`);
```

---

## 🛠️ 技术栈

```
┌───────────────────────────────────────┐
│         前端 (Browser)                  │
│  ┌─────────┬──────────┬──────────┐    │
│  │ HTML5   │   CSS3   │ Chart.js │    │
│  └─────────┴──────────┴──────────┘    │
│                ↕ HTTP/JSON              │
│  ┌────────────────────────────────┐    │
│  │     Flask (Python 后端)        │    │
│  └────────────────────────────────┘    │
│                ↕                        │
│  ┌────────────────────────────────┐    │
│  │    psutil (系统数据采集)        │    │
│  │  ┌────┬─────┬─────┬──────┐   │    │
│  │  │CPU │内存 │磁盘 │网络  │   │    │
│  │  └────┴─────┴─────┴──────┘   │    │
│  └────────────────────────────────┘    │
│         操作系统内核 (OS Kernel)        │
└───────────────────────────────────────┘
```

| 层级 | 技术 | 用途 |
|------|------|------|
| 🖥️ **后端** | Python Flask | HTTP 服务、RESTful API |
| 📡 **数据采集** | psutil | CPU、内存、磁盘、网络、进程信息 |
| 🎨 **前端** | HTML5 + CSS3 | 响应式深色主题仪表盘 |
| 📊 **图表** | Chart.js | CPU & 内存历史趋势折线图 |
| 🔄 **通信** | Fetch API | 每 2 秒异步拉取 JSON 数据 |

---

## ❓ 常见问题

<details>
<summary><b>Q: 启动时报错 "Address already in use"</b></summary>

端口 5000 被占用了。修改端口启动：
```bash
PORT=8080 python app.py
```
</details>

<details>
<summary><b>Q: 局域网其他设备无法访问</b></summary>

1. 确认使用的是 **局域网 IP**（如 192.168.x.x），而不是 127.0.0.1
2. 检查防火墙是否放行了端口：
   ```bash
   # Linux 临时放行
   sudo ufw allow 5000
   ```
3. 确认所有设备在同一网络下
</details>

<details>
<summary><b>Q: CPU 温度显示 N/A</b></summary>

部分虚拟机或云服务器不支持读取 CPU 温度，这是正常现象。如果是实体机，可检查是否缺少 `lm-sensors`：
```bash
sudo apt install lm-sensors
sudo sensors-detect
```
</details>

<details>
<summary><b>Q: 如何让服务开机自启？</b></summary>

**Linux (systemd)：**
```bash
# 创建服务文件
sudo tee /etc/systemd/system/resource-monitor.service <<EOF
[Unit]
Description=Resource Monitor Dashboard
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=/path/to/resource-monitor
ExecStart=/path/to/resource-monitor/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable --now resource-monitor
```

**Windows：**
创建一个 `start.bat` 放在启动文件夹即可。
</details>

<details>
<summary><b>Q: 如何在 Windows 上运行？</b></summary>

推荐使用 **WSL**（本项目的开发环境）。也可以直接在 Windows 上运行：
```powershell
# 用 PowerShell 或 cmd
py -3 -m venv venv
venv\Scripts\activate
pip install flask psutil
python app.py
```
</details>

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源 — 你可以自由使用、修改、分发，甚至用于商业项目。

```
MIT License

Copyright (c) 2026 MgAlNa3PO4

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

<div align="center">

**如果这个项目对你有帮助，欢迎 ⭐ Star 支持！**

[![GitHub Stars](https://img.shields.io/github/stars/MgAlNa3PO4/Local-resource-monitoring-system?style=social)](https://github.com/MgAlNa3PO4/Local-resource-monitoring-system)

🛠️ 由 [MgAlNa3PO4](https://github.com/MgAlNa3PO4) 维护 · 💡 欢迎提 Issue 或 PR

</div>
