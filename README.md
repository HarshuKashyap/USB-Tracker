# 🔌 USB Tracker – A Forensic USB File Activity Logger

USB Tracker is a Python-based cyber forensics tool designed to monitor and log file activities happening through USB devices connected to your system.

It is helpful for:
- Detecting unauthorized USB file access
- Digital forensic investigations
- Monitoring file transfers on secure machines

---

## 🚀 Features

- 🔍 Detects when a USB is inserted or removed
- 📁 Tracks file copy, move, delete operations on USB drives
- 📊 Logs time, action type, file name, and location
- 🧾 Generates logs in a readable format (CSV or TXT)
- 🔐 Works as a basic forensic tool for investigation

---

## 🛠️ Technologies Used

- Python 3.x
- OS and Platform modules
- `psutil` for device detection
- File handling and system logging

---

## 📦 Requirements

Before running the project, make sure you have Python installed. Then, install the required Python libraries using:

```bash
pip install -r requirements.txt
py usb_tracker.py

Sample Output Log

[2025-07-12 12:45:10] USB inserted: E:\
[2025-07-12 12:46:01] File copied: E:\Documents\report.docx
[2025-07-12 12:47:30] File deleted: E:\Pictures\old_image.png
[2025-07-12 12:50:22] USB removed: E:\
