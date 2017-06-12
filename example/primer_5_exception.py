# 5.1 异常处理概述
# 5.2 异常处理格式
'''
    try:
        程序
    except Exception as 异常名称:
        异常处理部分
'''
# URLError与HTTPError
'''
    两者都是异常处理的类, HTTPError是URLError的子类,HTTPError有异常状态码与异常原因,URLError没有异常状态码,所以
    在处理时,不能使用URLError代替HTTPError。如果要代替,必须要判断是否有状态码属性
'''
# try:
#     for i in range(0, 9):
#         if(i == 4):
#             print(i)
# except Exception as e:
#     print(e)
# print("ok")

#会抛出403异常，这个网址已屏蔽爬虫，必须伪装成浏览器
import urllib.request
import urllib.error

try:
    urllib.request.urlopen('http://blog.csdn.net')
except urllib.error.HTTPError as e:
    print(e.getcode())

try:
    url = 'http://blog.csdn.net'
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    data = urllib.request.urlopen(req).read().decode()
    print(data)
except urllib.error.HTTPError as e:
    print(e.getcode())
