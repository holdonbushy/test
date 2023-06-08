class Person:
    def getself(self):  
        print(id(self))

xw = Person()
xw.getself()
print(id(xw))
xc = Person()
print(id(xc))