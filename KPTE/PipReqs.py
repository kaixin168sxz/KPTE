# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import time
from py7zr import unpack_7zarchive
import os,shutil

def Get(files):
    subprocess.run(f'pipreqs {files} --encoding=utf8 --use-local', shell=True)

    shutil.move(os.path.join(files, 'requirements.txt'), os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements_copy.txt'))


def Move(OutputCodePath):
    shutil.move(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements_copy.txt'), os.path.join(OutputCodePath, 'requirements.txt'))

def MAKEFILE(OPEP):
    path = os.path.dirname(os.path.abspath(__file__)) + '\Data'
    print(os.path.dirname(os.path.abspath(__file__)))
    print(path)
    NOWPATH = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)
    shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
    shutil.unpack_archive('Python.7z', OPEP)
    os.chdir(NOWPATH)
