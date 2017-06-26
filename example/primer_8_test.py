#利用正则简单爬取数据
import re
import urllib.request
import urllib.error

# 自动提取课程页面的QQ群号码
'''
data = urllib.request.urlopen("http://edu.csdn.net").read() #查出整个页面的document
#print(data)
data = urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/253").read().decode("UTF-8")
#print(data)
pat = "<p>\d*</p>"
res = re.compile(pat).findall(data)
#print(res)
'''

#爬取豆瓣数据
'''
data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
#print(data)
pat = '<div class="name">(.*?)</div>'
res = re.compile(pat).findall(data)
#print(res)

wf = open('D:/douban.txt','w')
for i in range(0,len(res)):
    wf.write(res[i]+',')
wf.close()
'''

# urlretrieve(网址, 存储位置) 直接下载网页到本地

#urllib.request.urlretrieve("http://www.baidu.com", "存储位置")

# urlcleanup() 清除由于urllib.urlretrieve()所产生的缓存
# urllib.request.urlcleanup()

# info() 查看网页简介信息

'''
file = urllib.request.urlopen("https://read.douban.com/provider/all")
print(file.info)
print(file.getcode())
print(file.geturl())
'''

# 爬取CSDN的文章并存储于本地
'''
url = 'http://blog.csdn.net/'
header = ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [header]
data = opener.open(url,timeout=3).read().decode()
pat = '<h3  class="tracking-ad" data-mod="popu_254"><a href="(.*?)"'
res = re.compile(pat).findall(data)
# pat_nikename = 'class="nickname">(.*?)</a>'
# res_nikename = re.compile(pat_nikename).findall(data)
# print(res_nikename)
path = 'D:/python_cache/cache'

for i in range(0, len(res)):
    print(res[i])
    urllib.request.urlretrieve(res[i], path+str(i))
    print('第'+str(i+1)+'篇文章爬取成功')
'''

# 爬取美女图片
'''
url = 'http://www.mmjpg.com/'
header = ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [header]
data = opener.open(url).read().decode()
pat = '<a href="(.*?)" target='
res = re.compile(pat).findall(data)
path = 'D:/python_cache/cache/'
#res = list(set(res))#去重方法一，但以前的顺序是乱的
if len(res)>0 :
    for i in range(len(res)):
        try:
            data_ = opener.open(res[i]).read().decode()
            pat_ =  '<a href="'+res[i]+'/2"><img src="(.*?)"'
            res_ = re.compile(pat_).findall(data_)
            if len(res_):
                for j in range(len(res_)):
                    print(res_[j])
                    urllib.request.urlretrieve(res_[j], path + str(i) + '.jpg')
                    print('第'+str(i+1)+'张下载成功')
        except urllib.error.HTTPError as e:
            print(e.getcode())
'''

# 爬取䊭事百科
'''
header = ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [header]
mue = open('D:/python_cache/cache/mue.txt','w')
for i in range(0,2):
    url = 'https://www.qiushibaike.com/8hr/page/str(i+1)/'
    data = opener.open(url).read().decode()
    pat = '<span>(.*?)</span>'
    res = re.compile(pat).findall(data)
    mue.writelines(res)
    # for j in range(0, len(res)):
    #     mue.write(res(j))
    #     print('第'+str(j+1)+'条记录写入成功！')
'''

#今日头条
url = 'https://www.toutiao.com/api/pc/feed/'
header = ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [header]
data = opener.open(url).read().decode('gbk')
print(data)



