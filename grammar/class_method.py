class Person:
    def say_hi(self):
        print('Hi')


p = Person()
p.say_hi()
# 第二种调用实例方法的方式
Person.say_hi(p)
