import os
import shutil
import subprocess
import time


def Get(files):
    print('生成一个requirements.txt文件 >')

    print(f'执行cmd命令: pipreqs {files} --encoding=utf8')

    subprocess.Popen(f'pipreqs {files} --encoding=utf8')

    time.sleep(2)

    shutil.move(os.path.join(files, 'requirements.txt'), os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements_copy.txt'))


def Move(OutputCodePath):
    shutil.move(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements_copy.txt'), os.path.join(OutputCodePath, 'requirements.txt'))

    print('文件requirements.txt生成成功!')
    input('请查看requirements.txt, 如果有缺少项目的依赖包, 请在文本末尾添加:模块名==模块版本, 请在查看并修改后按下回车继续 >>>')
