class studentscourse:
    def __init__(self, name, course, age):
        self.name = name
        self.course = course
        self.age = age

    def studentsinfo(self):
        print("Name of student:", self.name, "course:",
              str(self.course), "age:", str(self.age))


student1 = studentscourse("Сейтова Салтанат", 4, 19)
student2 = studentscourse("Муратбаев Ален", 4, 20)

print(student1.age)
print(student2.course)

student1.studentsinfo()
