# project question

# Create a program to manage student records.
# Requirements
# Create a class named Student.
# Each student should have
# Student ID
# Name
# Age
# Course
# Marks
# Create another class called StudentManagement.
# It should have methods to
# Add a student
# Display all students
# Search student using Student ID
# Update marks
# Delete a student
# Display topper
# Store all students inside a list.
# Bonus
# Calculate average marks.
# Display Pass/Fail (Pass if marks >= 40).

class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_details(self):
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.marks}")
        if self.marks >= 40:
            print("Result     : Pass")
        else:
            print("Result     : Fail")

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ")
        age = int(input("Enter Age : "))
        course = input("Enter Course : ")
        marks = int(input("Enter Marks : "))

        student = Student(student_id, name, age, course, marks)
        self.students.append(student)
        print("Student Added Successfully!")

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists.")

    def display_all_students(self):
        if len(self.students) == 0:
            print("No Student Records Found.")
        else:
            for student in self.students:
                student.display_details()
                print("----------------------------")

    def search_student(self):
        student_id = int(input("Enter Student ID to Search : "))

        for student in self.students:
            if student.student_id == student_id:
                print("Student Found")
                student.display_details()
                return

        print("Student Not Found.")

    def update_marks(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                new_marks = int(input("Enter New Marks : "))
                student.marks = new_marks
                print("Marks Updated Successfully.")
                return

        print("Student Not Found.")

    def delete_student(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully.")
                return

        print("Student Not Found.")

    def display_topper(self):
        if len(self.students) == 0:
            print("No Student Records Found.")
            return

        topper = self.students[0]

        for student in self.students:
            if student.marks > topper.marks:
                topper = student

        print("Topper Details")
        topper.display_details()

    def average_marks(self):
        if len(self.students) == 0:
            print("No Student Records Found.")
            return

        total = 0

        for student in self.students:
            total += student.marks

        average = total / len(self.students)
        print(f"Average Marks : {average:.2f}")


obj = StudentManagement()

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Average Marks")
    print("8. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        obj.add_student()

    elif choice == 2:
        obj.display_all_students()

    elif choice == 3:
        obj.search_student()

    elif choice == 4:
        obj.update_marks()

    elif choice == 5:
        obj.delete_student()

    elif choice == 6:
        obj.display_topper()

    elif choice == 7:
        obj.average_marks()

    elif choice == 8:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
