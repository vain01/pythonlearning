class Person:
    name = 'a'

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi', self.name)


p = Person('hao')
p.say_hi()
# Person('liang').say_hi()
print(p.name)
print(Person.name)
