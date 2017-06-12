'''
1.urllib.urlencode(query, doseq=0)
接受参数形式为：[(key1, value1), (key2, value2),...] 和 {'key1': 'value1', 'key2': 'value2',...}
返回的是形如'key2=value2&key1=value1'字符串。
urllib.urlencode({'name': u'老王'.encode('utf8'), 'sex': u'男'.encode('utf8')})
'name=%E8%80%81%E7%8E%8B&sex=%E7%94%B7'

2.urllib.quote(s, safe='/')
接受参数s为字符串，safe是指定某字符不被urlencode，默认为'/'，
如指定'+'、'/'不需转换，传 '+/' 和 '+ /' 均可。另外此方法会将“空格”转换为“%20”
urllib.quote(u'老王 /+'.encode('utf8'))
'%E8%80%81%E7%8E%8B%20/%2B'

3.urllib.quote_plus(s, safe='')
此方法的源码为:
def quote_plus(s, safe=''):
    """Quote the query fragment of a URL; replacing ' ' with '+'"""
    if ' ' in s:
        s = quote(s, safe + ' ')
        return s.replace(' ', '+')
    return quote(s, safe)
可以看出它比quote多一些功能，但是会将“空格”转换成“加号”，默认safe为空。
 urllib.quote_plus(u'老王 /+'.encode('utf8'))
'''

# python3
# urllib.request
# 网络请求操作
#
# 基本的网络请求示例
#
# 复制代码
# '''
# Created on 2014年4月22日
#
# @author: dev.keke@gmail.com
# '''
# import urllib.request
#
# # 请求百度网页
# resu = urllib.request.urlopen('http://www.baidu.com', data=None, timeout=10)
# print(resu.read(300))
#
# # 指定编码请求
# with urllib.request.urlopen('http://www.baidu.com') as resu:
#     print(resu.read(300).decode('GBK'))
#
# # 指定编码请求
# f = urllib.request.urlopen('http://www.baidu.com')
# print(f.read(100).decode('utf-8'))
# 复制代码
# 发送数据请求，CGI程序处理
#
# 复制代码
# >> > import urllib.request
# >> > req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',
#                                   ...
# data = b'This data is passed to stdin of the CGI')
# >> > f = urllib.request.urlopen(req)
# >> > print(f.read().decode('utf-8'))
# Got
# Data: "This data is passed to stdin of the CGI"
# 复制代码
# PUT请求
#
# 复制代码
# import urllib.request
#
# DATA = b'some data'
# req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
# f = urllib.request.urlopen(req)
# print(f.status)
# print(f.reason)
# 复制代码
# 基本的HTTP验证，登录请求
#
# 复制代码
# import urllib.request
#
# # Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)
# urllib.request.urlopen('http://www.example.com/login.html')
# 复制代码
# 支持代理方式验证请求
#
# 复制代码
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
#
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# # This time, rather than install the OpenerDirector, we use it directly:
# opener.open('http://www.example.com/login.html')
# 复制代码
# 添加
# http
# headers
#
# import urllib.request
#
# req = urllib.request.Request('http://www.example.com/')
# req.add_header('Referer', 'http://www.python.org/')
# r = urllib.request.urlopen(req)
# 添加
# user - agent
#
# import urllib.request
#
# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# opener.open('http://www.example.com/')
# 带参数的GET
# 请求
#
# >> > import urllib.request
# >> > import urllib.parse
# >> > params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# >> > f = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
# >> > print(f.read().decode('utf-8'))
# 带参数的POST请求
#
# 复制代码
# >> > import urllib.request
# >> > import urllib.parse
# >> > data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# >> > data = data.encode('utf-8')
# >> > request = urllib.request.Request("http://requestb.in/xrbl82xr")
# >> >  # adding charset parameter to the Content-Type header.
# >> > request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
# >> > f = urllib.request.urlopen(request, data)
# >> > print(f.read().decode('utf-8'))
# 复制代码
# 指定代理方式请求
#
# >> > import urllib.request
# >> > proxies = {'http': 'http://proxy.example.com:8080/'}
# >> > opener = urllib.request.FancyURLopener(proxies)
# >> > f = opener.open("http://www.python.org")
# >> > f.read().decode('utf-8')
# 无添加代理
#
# >> > import urllib.request
# >> > opener = urllib.request.FancyURLopener({})
# >> > f = opener.open("http://www.python.org/")
# >> > f.read().decode('utf-8')

#post请求
import urllib.request
import urllib.parse
import re

posturl = "http://httpbin.org/post"

# post请求的参数, 当参数中有中文时,记得需要做encode处理
postdata = urllib.parse.urlencode({'name':'张三','age':18}).encode('utf-8')
req = urllib.request.Request(posturl,postdata)
rst = urllib.request.urlopen(req).read().decode('utf-8')
#print(rst)


#发送get请求
keyword = "python"
keyword = urllib.request.quote(keyword)

# 分页获取10页数据 page = (num - 1) * 10
for i in range(1, 2):
    url = "https://www.baidu.com/s?wd=" + keyword + "&pn=" + str((i - 1) * 10)
    req = urllib.request.Request(url)
    # 必须要设置user-agent,不然获取不到数据
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    data = urllib.request.urlopen(req).read().decode("utf-8")
    print(data)
    pat1 = "title:'(.*?)',"
    rst1 = re.compile(pat1).findall(data)

    for j in range(0, len(rst1)):
        print(rst1[j])





