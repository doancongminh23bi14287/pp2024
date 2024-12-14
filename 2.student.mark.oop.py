class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Dictionary to store marks by course ID

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_students(self, num_students):
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student's name: ")
            dob = input("Enter student's Date of Birth (DD/MM/YYYY): ")
            student = Student(student_id, name, dob)
            self.students.append(student)
        print(f"{num_students} students added successfully!")

    def add_courses(self, num_courses):
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)
        print(f"{num_courses} courses added successfully!")

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
            print(f"Course ID: {course.course_id}, Course Name: {course.name}")

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

    def get_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def main_menu(self):
        while True:
            print("\nStudent Mark Management System")
            print("1. Input number of students and their information")
            print("2. Input number of courses and their information")
            print("3. Input marks for a selected course")
            print("4. List all courses")
            print("5. List all students")
            print("6. Show student marks for a given course")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                num_students = int(input("Enter number of students: "))
                self.add_students(num_students)

            elif choice == "2":
                num_courses = int(input("Enter number of courses: "))
                self.add_courses(num_courses)

            elif choice == "3":
                self.list_courses()
                course_id = input("Enter course ID to input marks: ")
                self.input_marks_for_course(course_id)

            elif choice == "4":
                self.list_courses()

            elif choice == "5":
                self.list_students()

            elif choice == "6":
                self.list_courses()
                course_id = input("Enter course ID to view marks: ")
                self.show_student_marks(course_id)

            elif choice == "7":
                print("Exiting the system.")
                break

            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.main_menu()
