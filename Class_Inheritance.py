class member:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        member.count+=1

    def tell(self):
        print("Name - {}, Age - {}".format(self.name, self.age), end=" ")

class student(member):
    def __init__(self, name, age, marks):
        member.__init__(self,name,age)
        self.marks = marks

    def tell(self):
        member.tell(self)
        print("Marks - {}".format(self.marks))

class teacher(member):
    def __init__(self,name, age, salary):
        member.__init__(self,name,age)
        self.salary = salary

    def tell(self):
        member.tell(self)
        print("salary - {}".format(self.salary))

s = student('Kapil', 21, 75)
t = teacher('Rajesh', 50, 10000000)

members = [s,t]
for i in members:
    i.tell()
print(teacher.count)

