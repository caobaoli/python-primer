'''
2.1 python 的基本控制流（顺序、选择、循环）
'''
# if语句的使用
'''
a = 100
b = 90
if(a > 200):
    print(a)
    if(b > 0):
        print(b)
elif(a < 90):
    print("a > 90")
else:
    print("it is ok")
'''

# 循环语句 while的使用
'''
i = 10
while(i > 0):
    print(i)
    i = i - 10
'''

# 循环语句for的使用
'''
a = ['11','22','33','44']
for i in a :
    print(i)
'''

# for 进行常规循环
'''
for i in range(1, 5):
    print("hello world!")
'''

# 中断结构
# 指的是中途退出的一种结构, 常有break语句与continue语句
'''
a = ['a1','a2','a3','a4']
for i in a:
    if(i == 'a3'):
        break
    print(i)
print('-------------------------')

for i in a:
    if(i == 'a3'):
        continue
    print(i)
'''

#输出乘法口诀
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) + ' * ' + str(j) + ' = ' + str(i * j), end = " ")
    print()#换行
'''

# 2.2 函数的使用
'''
i = 1000
def fun():
    j = 100
    print(j)
print(i)
fun()
'''
def func2(a, b):
    if(a > b):
        print("a 大于 b")
    elif( a == b):
        print("a 等于 b")
    else:
        print("a 小于 b")
# a=1, b=10
func2(1, 10)








