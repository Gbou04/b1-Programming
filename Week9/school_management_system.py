#Step 1: Create the base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"Hello, My Name is {self.name} and I am {self.age} years old."

#Step 2: Build the student class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hello, I am {self.name} and I am a student. My ID is {self.student_id} and I am {self.age} years old. "

#step 3: build teacher class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"I am {self.name} and I am a {self.subject} teacher. I am {self.age} years old."

#step 4: test your classes
student = Student("Alice", 16, "S001")
teacher = Teacher("Mr.Smith", 35, "Mathematics")

print("=== School Management System ===")
print(student.introduce())
print(teacher.introduce())