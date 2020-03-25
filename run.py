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
        install_package('msvcrt')
else:
    try:
        import getch
    except ImportError as e:
        install_package('getch')

import main
