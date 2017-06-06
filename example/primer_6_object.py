# 6.1 类与对象
# 类的定义
class cls:
    pass

# 类的实例化
a = cls()

# 构造函数(构造方法)
# self 在类中的方法必须加上self参数
# __init__(self, 参数)
class c1:
    def __init__(self):
        print("hello world")

#给构造方法加参数
class c2:
    def __init__(self, name):
        print("name:" + name)


# 6.2 属性与方法
class c3:
    def __init__(self, name):
        self.name = name

class c4:
    def __init__(self, name):
        self.myname = name
    def show(self, name):
        print("hello " + self.name)
# 6.3 继承

#单继承
class father:
    def speak(self):
        print("hahahahaha")
class son(father):
    pass
d = son()
#d.speak()

#多继承
class mother:
    def say(self):
        print("say mother")
class son_(father,mother):
    def speak(self):
        print("say father")
s = son_()
s.speak()
s.say()
