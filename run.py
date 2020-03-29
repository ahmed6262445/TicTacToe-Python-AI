import sys
import subprocess
from os import system
import platform

def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


os_name = platform.system().lower()
if os_name == 'windows':
    try:
        import msvcrt 
    except ImportError as e:
        print("Installing msvcrt...")
        install_package('msvcrt')
else:
    try:
        import getch
    except ImportError as e:
        print("Installing getch...")
        install_package('getch')
try:
    import numpy
except ImportError as e:
    print("Installing numpy...")
    install_package('getch')

import main
