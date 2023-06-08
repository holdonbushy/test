class Person:
    def __init__(self,name,sex=None,age=None):
        self.name = name
        self.sex = sex
        self.age = age
        print('--init--函数执行')
    #实例方法
    def __str__(self):
        print('--str--函数的执行')
        return f'我叫{self.name}'
    
    
    def __new__(cls,*args, **kwargs):
        print('--new--函数的执行')
        return object.__new__(cls)

    def eat(self):
        print("吃饭")
        pass

xm = Person('小明')
print(xm)