from tkinter import *
import subprocess
import os
import sys

root = Tk()

root.title("Başlatıcı")
root.geometry("400x400")

# EXE'nin bulunduğu klasör
base_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)

def windows():
    exe = os.path.join(base_dir, "main", "Baslatici.exe")
    subprocess.Popen(exe)

def python():
    py = os.path.join(base_dir, "main", "Baslatici.py")
    subprocess.Popen(["python", py])

Button(
    root,
    text="Windows için Başlatıcı",
    command=windows
).pack(pady=10)

Button(
    root,
    text="Python için Başlatıcı",
    command=python
).pack(pady=10)

root.mainloop()