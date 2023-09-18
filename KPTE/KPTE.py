# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import shutil
import py7zr
import PipReqs
import sys

def KPTE():
    cmd_input = argparse.ArgumentParser(description='KaixinPyToExe 帮助:')
    cmd_input.add_argument('-p', '--path', type=str, metavar='', required=True, help='主文件的路径，必填')
    cmd_input.add_argument('-o', '--output', type=str, metavar='', required=True, help='exe文件输出路径，必填（放在单独文件夹内）')
    cmd_input.add_argument('-f', '--files', type=str, metavar='', required=True, help='项目文件夹路径，必填，其中的所有文件将会被打包（不可以有除了项目文件及依赖以外的大型文件夹[例如虚拟环境，多文件exe等]，否则将会报错或将其复制）')
    cmd_input.add_argument('-n', '--name', type=str, metavar='', default='RUN', help='exe文件名称，默认为RUN.exe')
    cmd_input.add_argument('-c', '--cmd', type=str, metavar='', default='c', help='是否显示cmd窗口，c为显示，w为不显示，默认为c')
    cmd_input.add_argument('-i', '--icon', type=str, metavar='', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.ico'), help='图标路径，有默认值（.ico格式）')

    args = cmd_input.parse_args()

    OutputPythonPath = os.path.join(args.output, 'Python')
    OutputCodePath = os.path.join(args.output, 'Code')
    OutputWhlPath = os.path.join(args.output, 'WhlFiles')
    OutputExePath = args.output


    print(f'path:{args.path}  output:{args.output}  files:{args.files}')
    print('开始打包...')

    if not os.path.isdir(args.output) and not os.path.isfile(args.path):
        print('路径错误')
        print('退出KaixinPyToExe')
        sys.exit()

    PipReqs.Get(args.files)


    print('复制文件中 >')

    src_folder = args.files
    dst_folder = os.path.dirname(os.path.abspath(__file__)) + '\\copy_'

    subprocess.call(['robocopy', src_folder, dst_folder, '/E'])

    shutil.move(os.path.dirname(os.path.abspath(__file__)) + '\\copy_', OutputCodePath)


    print('复制成功!')


    print('解压文件中 >')

    archive = py7zr.SevenZipFile(f'{os.path.dirname(os.path.abspath(__file__))}\\Python.7z', mode='r')
    archive.extractall(path=OutputExePath)
    archive.close()

    print('解压成功!')

    PipReqs.Move(args.files)


    os.makedirs(OutputWhlPath)

    print('Pip >')

    drive, path = os.path.splitdrive(args.files)

    print(f'运行cmd命令: {OutputPythonPath}\\python.exe -m pip download -r {os.path.join(args.files, "requirements.txt")} -i https://pypi.tuna.tsinghua.edu.cn/simple -d {OutputWhlPath}')
    subprocess.run(f'{OutputPythonPath}\\python.exe -m pip download -r {os.path.join(args.files, "requirements.txt")} -i https://pypi.tuna.tsinghua.edu.cn/simple -d {OutputWhlPath}')

    print('执行pip成功!')

    print('生成文件 >')

    PyPath = os.path.join(OutputExePath, f'{args.name}.py')


    print('生成Install.txt文件中 >')

    with open(os.path.join(OutputPythonPath, 'Install.txt'), 'w') as InstallFile:
        InstallFile.write("F")

    print('Install.txt文件生成成功!')

    Code = f"""import os
import subprocess

files = r"{OutputExePath}"

with open(os.path.join(r"{OutputPythonPath}", 'Install.txt'), 'r') as InstallFile:
    InstallRead = InstallFile.read()

if InstallRead == 'F':
    drive, path = os.path.splitdrive(files)

    Path = r"{args.files}"
    subprocess.run(drive, shell=True)
    subprocess.run(f'cd {{path}}', shell=True)
    subprocess.run(fr'.\Python\python.exe -m pip install --no-index --find-links={{os.path.join(files, "WhlFiles")}} -r {{os.path.join(Path, "requirements.txt")}}', shell=True)
    with open(os.path.join(r"{OutputPythonPath}", 'Install.txt'), 'w') as InstallFile:
        InstallFile.write("T")

subprocess.run(f'.\Python\python.exe -u .\Code\{os.path.basename(args.path)}', shell=True)
"""

    print('生成运行文件')

    with open(PyPath, 'w') as PyFile:
        PyFile.write(Code)

    print(f'文件:\n{Code}')


    print('运行文件生成成功!')


    print('Pyinstaller >')

    DistDir = OutputExePath

    print(OutputExePath)
    print(DistDir)


    print(f'运行cmd命令: pyinstaller --icon={args.icon} -F -{args.cmd} --distpath={DistDir} {PyPath}')

    subprocess.run(f'pyinstaller --icon={args.icon} -F -{args.cmd} --distpath={DistDir} {PyPath}')

    input('输入回车关闭 >>>')

    sys.exit()


KPTE()