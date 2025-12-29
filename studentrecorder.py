from screen_brightness_control import percentage


class Student:
    def __init__(self,name,roll_no,class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name

class ReportCard:
    def __init__(self,student):
        self.student = student
        self.marks = {}

    def add_marks(self):
        n = int(input("Enter number of subjects: "))
        for _ in range(n):
            subject = input("enter subject name: ")
            mark = int(input(f"enter marks for {subject}: "))
            self.marks[subject] = mark

    def calculate_total(self):
        return sum(self.marks.values())
    def calculate_percentage(self):
        total = self.calculate_total()
        return total / (len(self.marks) * 100) * 100
    def calculate_grade(self,percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "Fail"
    def calculate_result(self):
        for mark in self.marks.values():
            if mark < 40 :
                return "Fail"
        return "pass"
    def display_report(self):
        total = self.calculate_total()
        percentage = self.calculate_percentage()
        grade = self.calculate_grade(percentage)
        result = self.calculate_result()

        print("\n" + "-" * 40)
        print("        STUDENT REPORT CARD")
        print("-" * 40)
        print(f"Name      : {self.student.name}")
        print(f"Roll No   : {self.student.roll_no}")
        print(f"Class     : {self.student.class_name}")
        print("\nMarks:")

        for subject,mark in self.marks.items():
            print(f"{subject:<12}:{mark}")

        print("\nTotal     :", total)
        print(f"Percentage: {percentage:.2f}%")
        print("Grade     :", grade)
        print("Result    :", result)
        print("-" * 40)

name = input("enter student name")
roll = input("enter roll number: ")
class_name = input("enter class: ")
student = Student(name,roll,class_name)
report = ReportCard(student)
report.add_marks()
report.display_report()