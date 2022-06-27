import random


for x in range(10):
    y = x * x
    print(y)


class Student:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.counter += 1


s1 = Student("Maik", 20)
s2 = Student("Kira", 19)
li_students = ["Kay", "Horst", "Steph"]
for name in li_students:
    st = Student(name, random.randint(19, 25))
print(f"Number of Students: {Student.counter}")
