# python-primer

####
	python 版本：3.6
	推荐使用IDE：pyCharm（与eclipse等IDE相似，有编译异常提醒，运行简单，可以断点跟踪）
	特别注明：相关知识点参考于(https://github.com/gaoyaqiu/python-spider) 
###
	关于将python文件打包exe文件步骤：
	    windows环境下在cmd命令窗口：
	           1、安装pyinstaller
	                pip install pyinstaller 
	           2、执行build命令，并添加必要的搜索路径，外加执行文件的图标：
	                cd D:\tmp\core-wxpython
                    pyinstaller -F -w -i d:\tmp\main.ico main.py
                  如果还想添加自定义的依赖库，就要加上-p参数：
                    pyinstaller -F -w -p D:\tmp\core-python\libs -i d:\tmp\main.ico main.py
                  (参数说明：
                    -F 表示生成单个可执行文件
                    -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
                    -p 表示你自己自定义需要加载的类路径，一般情况下用不到
                    -i 表示可执行文件的图标)
               3、目前pyinstaller只支持到3.5.2,要想支持最新版本(比如目前最新版3.6)请到https://github.com/pyinstaller/pyinstaller
                  下载并解压zip并将PyInstaller与(Python安装目录)Python36\Lib\site-packages下的PyInstaller替换即可。
               4、http://www.cnblogs.com/dacainiao/p/5918845.html(可以参考此网站内容)
	                            
	             
