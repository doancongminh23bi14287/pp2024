import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to store marks by course ID

    def add_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10  # Round down to 1 decimal

    def calculate_gpa(self, course_credits):
        total_credits = sum(course_credits.values())
        weighted_sum = sum(self.marks[course_id] * course_credits[course_id] for course_id in self.marks if course_id in course_credits)
        return weighted_sum / total_credits if total_credits > 0 else 0

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_students(self, num_students):
        try:
            for _ in range(num_students):
                student_id = input("Enter student ID: ")
                name = input("Enter student's name: ")
                dob = input("Enter student's Date of Birth (DD/MM/YYYY): ")
                student = Student(student_id, name, dob)
                self.students.append(student)
            print(f"{num_students} students added successfully!")
        except Exception as e:
            print(f"Error adding students: {e}")

    def add_courses(self, num_courses):
        try:
            for _ in range(num_courses):
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                credits = int(input("Enter course credits: "))
                course = Course(course_id, course_name, credits)
                self.courses.append(course)
            print(f"{num_courses} courses added successfully!")
        except Exception as e:
            print(f"Error adding courses: {e}")

    def input_marks_for_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if not course:
            print("Course not found!")
            return

        print(f"Input marks for course: {course.name}")
        for student in self.students:
            try:
                mark = float(input(f"Enter marks for student {student.name} (ID: {student.student_id}): "))
                student.add_mark(course_id, mark)
            except ValueError:
                print("Invalid mark entered. Please enter a number.")
        print("Marks entered successfully!")

    def list_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        print("\nList of Courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.name}, Credits: {course.credits}")

    def list_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\nList of Students:")
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks(self, course_id):
        course = self.get_course_by_id(course_id)
        if not course:
            print("Course not found!")
            return

        print(f"\nMarks for Course: {course.name}")
        for student in self.students:
            marks = student.marks.get(course_id, None)
            if marks is not None:
                print(f"Student {student.name} (ID: {student.student_id}) - Marks: {marks}")
            else:
                print(f"Student {student.name} (ID: {student.student_id}) - No marks entered.")

    def sort_students_by_gpa(self):
        course_credits = {course.course_id: course.credits for course in self.courses}
        self.students.sort(key=lambda student: student.calculate_gpa(course_credits), reverse=True)

        print("\nStudents sorted by GPA:")
        for student in self.students:
            gpa = student.calculate_gpa(course_credits)
            print(f"Student {student.name} (ID: {student.student_id}) - GPA: {gpa:.2f}")

    def get_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def main_menu(self, stdscr):
        curses.curs_set(0)
        current_row = 0
        menu = [
            "Input number of students and their information",
            "Input number of courses and their information",
            "Input marks for a selected course",
            "List all courses",
            "List all students",
            "Show student marks for a given course",
            "Sort students by GPA",
            "Exit",
        ]

        while True:
            stdscr.clear()
            stdscr.addstr("Student Mark Management System\n", curses.A_BOLD)
            for idx, item in enumerate(menu):
                if idx == current_row:
                    stdscr.addstr(f"> {item}\n", curses.color_pair(1))
                else:
                    stdscr.addstr(f"  {item}\n")

            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    num_students = int(input("Enter number of students: "))
                    self.add_students(num_students)
                elif current_row == 1:
                    num_courses = int(input("Enter number of courses: "))
                    self.add_courses(num_courses)
                elif current_row == 2:
                    self.list_courses()
                    course_id = input("Enter course ID to input marks: ")
                    self.input_marks_for_course(course_id)
                elif current_row == 3:
                    self.list_courses()
                elif current_row == 4:
                    self.list_students()
                elif current_row == 5:
                    self.list_courses()
                    course_id = input("Enter course ID to view marks: ")
                    self.show_student_marks(course_id)
                elif current_row == 6:
                    self.sort_students_by_gpa()
                elif current_row == 7:
                    break

            stdscr.refresh()

if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    curses.wrapper(system.main_menu)
