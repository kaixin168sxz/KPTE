# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import shutil
import sys

try:
    import PipReqs
except ImportError:
    from KPTE import PipReqs
Run = True


def KPEC(Path, Files=None, OutPut=None, Icon=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data\icon.ico'), Name=None, Cmd='c', Type='cmd', PipFile=None): 
    global Type_, Run
    Type_ = Type
    if Files is None:
        Files = os.path.dirname(Path)

    if OutPut is None:
        OutPut = os.path.join(os.path.dirname(Path), 'dist')

    if Name is None:
        dirStr, ext = os.path.splitext(Path)
        Name = dirStr.split("\\")[-1]

    OutputPythonPath = os.path.join(OutPut, 'Python')
    OutputCodePath = os.path.join(OutPut, 'Code')
    OutputWhlPath = os.path.join(OutPut, 'WhlFiles')
    OutputExePath = OutPut

    print(f'path:{Path}  output:{OutPut}  files:{Files}')
    print('开始打包...')

    if not os.path.isdir(OutPut) and not os.path.isfile(Path):
        print('路径错误')
        print('退出KaixinPyToExe')
        sys.exit()

    if Type == 'cmd':
        print('生成一个requirements.txt文件 >')
        print(f'执行cmd命令: pipreqs {Files} --encoding=utf8 --use-local')
        PipReqs.Get(Files)


    print('复制文件中 >')

    src_folder = Files
    dst_folder = os.path.dirname(os.path.abspath(__file__)) + '\\copy_'

    subprocess.call(['robocopy', src_folder, dst_folder, '/E'])

    shutil.move(os.path.dirname(os.path.abspath(__file__)) + '\\copy_', OutputCodePath)


    print('复制成功!')
    print('解压文件中 >')

    print(f'{os.path.dirname(os.path.abspath(__file__))}\\Data\\Python.7z')
    PipReqs.MAKEFILE(OPEP=OutputExePath)

    print('解压成功!')
    
    if Type == 'cmd':
        PipReqs.Move(Files)
        print('文件requirements.txt生成成功!')
        input('请查看requirements.txt, 如果有缺少项目的依赖包, 请在文本末尾添加:模块名==模块版本, 请在查看并修改后按下回车继续 >>>')
        
    os.makedirs(OutputWhlPath)

    print('Pip >')
    
    with open(os.path.join(Files, "requirements.txt"), 'r') as PipFileData:
        PipList = PipFileData.read().split('\n')
        for i in PipList:
            print(f'运行cmd命令: {OutputPythonPath}\\python.exe -m pip install {i} -i https://pypi.tuna.tsinghua.edu.cn/simple --no-warn-script-location')
            subprocess.run(f'{OutputPythonPath}\\python.exe -m pip install {i} -i https://pypi.tuna.tsinghua.edu.cn/simple --no-warn-script-location')

    print('执行pip成功!')

    print('生成文件 >')

    PyPath = os.path.join(OutputExePath, f'{Name}.py')


    print('生成Install.txt文件中 >')

    with open(os.path.join(OutputPythonPath, 'Install.txt'), 'w') as InstallFile:
        InstallFile.write("F")

    print('Install.txt文件生成成功!')

    Code = f"""import os
import subprocess

Path = os.path.dirname(os.path.abspath("."))
os.chdir(fr'{{Path}}\dist\Code')

subprocess.run(fr'..\Python\python.exe -u .\{Name}.py', shell=True)
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


    print(f'运行cmd命令: pyinstaller --icon={Icon} -F -{Cmd} --distpath={DistDir} {PyPath}')

    subprocess.run(f'pyinstaller --icon={Icon} -F -{Cmd} --distpath={DistDir} {PyPath}')

    if Type == 'cmd':
        input('按下回车退出 >>>')
        sys.exit()
    

def KPTE():
    cmd_input = argparse.ArgumentParser(description='KaixinPyToExe 帮助:')
    cmd_input.add_argument('-p', '--path', type=str, metavar='', required=True, help='主文件的路径，必填')
    cmd_input.add_argument('-o', '--output', type=str, metavar='', default=None, help='exe文件输出路径（放在单独文件夹内）')
    cmd_input.add_argument('-f', '--files', type=str, metavar='', default=None, help='项目文件夹路径，其中的所有文件将会被打包（不可以有除了项目文件及依赖以外的大型文件夹[例如虚拟环境，多文件exe等]，否则将会报错或将其复制）')
    cmd_input.add_argument('-n', '--name', type=str, metavar='', default=None, help='exe文件名称，默认为文件名')
    cmd_input.add_argument('-c', '--cmd', type=str, metavar='', default='c', help='是否显示cmd窗口，c为显示，w为不显示，默认为c')
    cmd_input.add_argument('-i', '--icon', type=str, metavar='', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data\icon.ico'), help='图标路径，有默认值（.ico格式）')
    cmd_input.add_argument('-t', '--type', type=str, metavar='', default='cmd', help='运行模式')

    args = cmd_input.parse_args()

    KPEC(Path=args.path, OutPut=args.output, Files=args.files, Name=args.name, Cmd=args.cmd, Icon=args.icon, Type=args.type)

if __name__ == '__main__':
    KPTE()