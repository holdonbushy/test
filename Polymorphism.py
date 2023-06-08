class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# 多态性的应用
def make_sound(animal):
    animal.sound()

# 创建不同类型的对象
dog = Dog()
cat = Cat()

# 调用 make_sound 函数
make_sound(dog)  # 输出：Dog barks
make_sound(cat)  # 输出：Cat meows
