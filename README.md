# 🖥️ Hardware Vitals Logger

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A lightweight, automated Python utility designed to continuously monitor and log core system hardware metrics (CPU usage, RAM allocation, and Battery status) into a structured CSV format for analysis. 

This project is ideal for tracking system performance over time, diagnosing hardware bottlenecks, or serving as a foundational script for larger desktop automation and monitoring systems.

## ✨ Key Features
* **Real-Time Monitoring:** Fetches live system data using direct OS hooks.
* **Low Overhead:** Runs quietly in the background without consuming significant resources.
* **Automated Data Logging:** Safely writes time-stamped hardware telemetry to `system_logs.csv`.
* **Hardware Agnostic:** Gracefully handles missing sensors (e.g., desktops without batteries).

## 🛠️ Prerequisites
This script requires Python 3.x and the `psutil` library to interface with the operating system's hardware sensors.

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/hardware-vitals-logger.git](https://github.com/yourusername/hardware-vitals-logger.git)
   cd hardware-vitals-logger# vitals_logger.py
