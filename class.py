

# class classname ():
     #def sayHello(self, a):  -> self is default paramater for functions:
         #print(a)


# In python everything is object
# functions is used to initializer to initialize objtect / rather than constructor in java which helps to create a object.

class hello():
    def __init__(self, a):
        self.var = a

    def say(self):
        print(self.var)


obj = hello("hi")
obj.say()
print(obj.var)