import subprocess

# Install PyQt5
subprocess.check_call(["python", "-m", "pip", "install", "pyqt5"])

# Install labelImg
subprocess.check_call(["python", "-m", "pip", "install", "labelImg"])

# Install ultralytics
subprocess.check_call(["python", "-m", "pip", "install", "ultralytics"])
