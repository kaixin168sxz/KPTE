# KaixinPyToExe(KPTE)使用手册

> 简介：**KaixinPyToExe用于将 `.py`文件转换为 `.exe`可执行文件**

## 使用须知：

* **运行平台**
  使用此方法打包**只适用于 `Windows xp`以上的 `64`位 `Windows`系统，暂不支持其他平台和 `32`位 `Winodws`系统**
* **兼容性**
  支持 `python-3.8`的语法，**不支持 ``python-3.8``后更新或以前的特殊语法或函数**
* **已在GitHub上开源**
  此项目使用 `MIT`协议，欢迎大家参考：**GitHub[项目地址](https://github.com/kaixin168sxz/KPTE)， 将其发布时请将 `MIT`协议证书放入!**

## 下载 `KPTE` 程序

* 可以通过 `pip` 命令来下载 `KPTE`：
  在 `cmd`中执行以下命令，来安装 `KPTE`模块：
  
  ```cmd
  pip install KPTE
  ```
  
  安装时**请确保 `pip`在环境变量中**

## 参数列表

```cmd
-h, --help 查看帮助并退出

-p , --path 主文件的路径，必填

-o , --output exe文件输出路径，必填（放在单独文件夹内）

-f , --files 项目文件夹路径，必填，其中的所有文件将会被打包（不可以有除了项目文件及依赖以外的大型文件夹[例如虚拟环 境，多文件exe等]，否则将会报错或将其复制）

-n , --name exe文件名称，默认为RUN.exe

-c , --cmd 是否显示cmd窗口，c为显示，w为不显示，默认为c

-i , --icon 图标路径，有默认值（.ico格式）
```

可以**通过cmd内执行 `KPTE -h` 或 `KPTE --help` 命令来获取**，具体方法见下

## 开始使用

开始前请确保python的Scripts文件夹在环境变量内

1. 使用 `-h` 或 `--help` 来查看帮助
   
   cmd内执行 `KPTE -h` 或 `KPTE --help` 命令，输出:
   
   ```cmd
   usage: KPTE.exe [-h] -p  -o  -f  [-n] [-c] [-i]
   
   KaixinPyToExe 帮助:
   
   optional arguments:
     -h, --help      show this help message and exit
     -p , --path     主文件的路径，必填
     -o , --output   exe文件输出路径，必填（放在单独文件夹内）
     -f , --files    项目文件夹路径，必填，其中的所有文件将会被打包（不可以有除了项目文件及依赖以外的大型文件夹[例如虚拟环
   境，多文件exe等]，否则将会报错或将其复制）
     -n , --name     exe文件名称，默认为RUN
     -c , --cmd      是否显示cmd窗口，c为显示，w为不显示，默认为c
     -i , --icon     图标路径，有默认值（.ico格式）
   ```

## 开始打包

执行以下命令进行打包:

```cmd
KPTE -p [你的主文件目录] -o [exe文件的输出路径(一个单独的文件夹)] -f [你的项目文件夹]
```

请将 `[xxx]`内的*替换* 为**你具体要填的值**

如看到:

```cmd
文件requirements.txt生成成功!
请查看requirements.txt, 如果有缺少项目的依赖包, 请在文本末尾添加:模块名==模块版本, 请在查看并修改后按下回车继续 >>>
```

请查看**项目文件夹下的看requirements.txt**如果其中**检测出的项目依赖有缺少**，请在其中**添加格式为`模块名==模块版本`**

cmd输出以下即可:

```cmd
9958 INFO: Building EXE from EXE-00.toc completed successfully.
输入回车关闭 >>>
```

**按下回车键关闭`KPTE`程序**

## 其他参数

> 请自行根据 `KPTE -h` 或 `KPTE --help` 命令中给出的提示，**自行测试**

## 其他

#### 关于

> 作者还在上五年级，更新可能较慢

**支持就在GitHub上给个星标吧，感谢大家的支持**

#### 版权声明

此项目由宋昕哲(Kaixin)开发，使用MIT协议，可商用

**但请在使用时不自称“自研”**，感谢您的配合，谢谢！
