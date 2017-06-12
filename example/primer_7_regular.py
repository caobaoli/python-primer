# 7.1 原子
'''
    原子是正则表达式中最基本的组成单位,每个正则表达式中至少要包含一个原子。
    常见的原子类型有:
        a. 普通字符作为原子
        b. 非打印字符作为原子
        c. 通用字符作为原子
        d. 原子表
'''
import re
string = 'yuanzi'
# 普通字符作为原子
pat = 'yuan'
rst = re.search(pat,string);
#print(rst)

# 非打印字符作为原子
# \n换行符， \t制表符
pat = '\n'
ret = re.search(pat,string)
#print(ret)

# 通用字符作为原子
'''
\w 匹配任意一个字母、数字、下划线
\W 匹配除字母、数字、下划线之外的任意字符
\d 十进制数
\D 除十进制以外的任意字符
\s 匹配空白字符
\S 匹配除空白以外的任意字符
'''

string = 'yuanzi568 767yuanziha'
pat = '\w\d\s\d\w'
rst = re.search(pat, string)
#print(rst)

# 原子表 从原子表中任意选一个原子来匹配
sting = 'yuanzi568767yuanziha'
pat = 'yua[n]zi'
rst = re.search(pat, string)
#print(rst)

# 7.2元字符
'''
    所谓元字符, 就是正则表达式中具有一些特殊含义的字符, 比如重复N次前面的字符等:
    . 除换行外任意一个字符
    ^ 开始位置
    $ 结束位置
    * 前面原子重复出现0次、1次或多次
    ? 前面原子重复出现0次、1次
    + 前面原子出现1次或多次
    {n} 前面原子恰好出现n次
    {n,} 前面原子至少n次
    {n, m} 最少出现n次,最多出现m次
    | 模式选择符 或
    () 模式单元
'''

string = 'yuanzi123456yuanzibaidu'
pat = 'yuan...'
pat = '^yuan...'
pat = 'ba...$'
pat = '123456+'
pat = "yuan{3,5}"
#rst = re.search(pat,string)
#print(rst)

# 模式修正符
'''
I 匹配时忽略大小写 *
M 多行匹配 *
L 本地化识别匹配
U unicode
S 让.匹配包括换行符 *
'''
string = 'python'
pat = 'PY'
rst = re.search(pat,string,re.I)
#print(rst)


# 正则表达式-贪婪模式和懒惰模式
# 默认就是贪婪模式
string = 'pythonc'
pat = 'p.*c'
rst = re.search(pat,string)
#print(rst)

#懒惰模式
pat = "p.*?c"
rst = re.search(pat, string, re.I)
#print(rst)



# 正则函数 re.match()、 re.search()、全局匹配、re.sub()
# match 从头开始匹配
# search 从任意地方匹配
string = 'pythonyjkjkjssa'
pat = "p.*?j"
rst = re.match(pat, string)
#print(rst)

# 全局匹配函数
string = 'sdpythpnyonyjkjkjptyssa'
pat = "p.*?y"
rst = re.compile(pat).findall(string)
#print(rst)

string = "<a href='http://www.baidu.com'>百度</a>"

pat = "[a-zA-z]+://[^\s]*[.com|.cn]"

ret = re.compile(pat).findall(string)

print(ret)

#匹配电话号码
string = "sdfsdfs021-123132432432fsfdwfds0773-23424324234sdfsdfsd"
pat = "\d{3}-\d{8}|\d{4}-\d{7}"
ret = re.compile(pat).findall(string)

print(ret)
##############################
'''
.*?与.*的区别
后边多一个？表示懒惰模式。
必须跟在*或者+后边用
如：<img src="test.jpg" width="60px" height="80px"/>
如果用正则匹配src中内容非懒惰模式匹配
src=".*"
匹配结果是：src="test.jpg" width="60px" height="80px"
意思是从="往后匹配，直到最后一个"匹配结束

懒惰模式正则：
src=".*?"
结果：src="test.jpg"
因为匹配到第一个"就结束了一次匹配。不会继续向后匹配。因为他懒惰嘛。
'''