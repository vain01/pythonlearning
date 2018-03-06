class Robot:
    '''Robot classs'''

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def __del__(self):
        print('Destroying robot', self.name)
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} is the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))

    @staticmethod
    def how_many():
        print('We have {0} robots.'.format(Robot.population))

    def say_hi(self):
        print('Call me', self.name)


r1 = Robot('R2')
r1.how_many()   #这个和Robot.how_many()的作用一样。不推荐使用，因为有可能会让其他人误认为how_many()是对象的方法
d2 = Robot('D2')
d2.say_hi()
Robot.how_many()

# 指定摧毁顺序
# r1 = Robot('R2')
# Robot.how_many()
# d2 = Robot('D2')
# Robot.how_many()
# del d2
#
