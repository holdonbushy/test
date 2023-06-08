class Person:
    def __init__(self,name,sex=None,age=None):
        self.name = name
        self.sex = sex
        self.age = age
    #实例方法
    def eat(self):
        print("吃饭")
        pass

xm = Person('小明')
xm.eat()
print(xm.name)