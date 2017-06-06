# 4.1 读取文件
# 打开文件
# open(文件名, 操作形式)
'''
w: 写入
r: 读取
b: 二进制
a: 追加
'''

# 文件读取可以用read(读取文件所有内容)和readline(按行读取)方法
# data = fh.read()
'''
rf = open("D:/python.txt","r")
while True:
    line = rf.readline()
    print(line)
    if not line:
        break
    pass
rf.close()
'''

#文件的写
'''
wf = open("D:/python.txt","w")
wf.write("hahahaha")
wf.close()
'''
wf = open("D:/python.txt","a+")
wf.write("能追加上去的呀")
wf.close()

