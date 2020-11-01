import os
from os.path import sep, join
import sys
import subprocess

basedir = os.path.dirname(os.path.abspath(__file__))
paths = [
    "KivyMD",
    f"kivymd-extensions{sep}KivyMD_Extensions",
    f"kivymd-extensions{sep}extension_template",
]
extensions_directory = f"kivymd-extensions{sep}extensions"
for dirname in os.listdir(extensions_directory):
    p = join(extensions_directory, dirname)
    if os.path.isdir(p):
        paths.append(p)

cmd = ["-m", "pip", "install", "-e"]
for p in paths:
    command = subprocess.list2cmdline([sys.executable, *cmd, join(basedir, p)])
    print(f'Running "{command}"')
    subprocess.check_call(command, cwd=basedir)
