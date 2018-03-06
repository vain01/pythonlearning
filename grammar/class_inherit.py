class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialize School Member:', self.name)

    def tell(self):
        print('Name: {0} Age:{1}'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialize Teacher:', self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:', self.salary)


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialize Student:', self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:', self.marks)


t = Teacher('Hao', 36, '18')
s = Student('Liang', 37, '21')
mermbers = [t, s]
for mermber in mermbers:
    mermber.tell()
