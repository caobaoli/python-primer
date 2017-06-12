import urllib.request
#伪装方式一
url = 'http://blog.csdn.net'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
data = urllib.request.urlopen(req).read().decode()
# print(data)

#伪装方式二
headers = ("User-Agen","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read().decode()
print(data)