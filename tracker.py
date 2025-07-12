import os, time
import win32file
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

class USBFileEventHandler(FileSystemEventHandler):
    def __init__(self, textbox):
        self.textbox = textbox

    def log(self, action, path):
        msg = f"{datetime.now()} - {action}: {path}\n"
        with open("log.txt", "a") as f:
            f.write(msg)
        self.textbox.insert(tk.END, msg)
        self.textbox.see(tk.END)

    def on_created(self, event):
        self.log("Created", event.src_path)

    def on_deleted(self, event):
        self.log("Deleted", event.src_path)

    def on_modified(self, event):
        self.log("Modified", event.src_path)

    def on_moved(self, event):
        self.log("Moved", f"{event.src_path} to {event.dest_path}")

def get_removable_drive():
    bitmask = win32file.GetLogicalDrives()
    for letter in range(26):
        if bitmask & (1 << letter):
            drive_letter = f"{chr(65 + letter)}:/"
            drive_type = win32file.GetDriveType(drive_letter)
            if drive_type == win32file.DRIVE_REMOVABLE:
                return drive_letter
    return None

def start_monitoring(textbox):
    drive = get_removable_drive()
    if not drive:
        textbox.insert(tk.END, "No USB drive found. Insert a USB drive first.\n")
        return

    textbox.insert(tk.END, f"Monitoring drive {drive}\n")
    event_handler = USBFileEventHandler(textbox)
    observer = Observer()
    observer.schedule(event_handler, path=drive, recursive=True)
    observer.start()

    def loop():
        while True:
            time.sleep(1)

    import threading
    threading.Thread(target=loop, daemon=True).start()

# GUI Code
root = tk.Tk()
root.title("USB Forensics Monitor")
textbox = ScrolledText(root, width=80, height=20)
textbox.pack()

start_btn = tk.Button(root, text="Start Monitoring", command=lambda: start_monitoring(textbox))
start_btn.pack()

root.mainloop()
