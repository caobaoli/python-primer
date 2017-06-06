# 5.1 异常处理概述
# 5.2 异常处理格式
'''
    try:
        程序
    except Exception as 异常名称:
        异常处理部分
'''
try:
    for i in range(0, 9):
        if(i == 4):
            print(i)
except Exception as e:
    print(e)
print("ok")
