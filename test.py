import subprocess
import sys

# List of packages to install
packages = ["streamlit", "Pillow", "Flask"]

# Install each package
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
