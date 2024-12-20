students = []
courses = []

def input_students(num_students):
    for _ in range(num_students):
        student_id = input("Enter student ID:")
        name = input("Enter student's name:")
        dob = input("Enter student's Date of Birth (DD/MM/YYYY):")
        student = {"id": student_id, "name": name, "dob": dob, "marks": {}}
        students.append(student)
    print(f"{num_students} students added successfully!")

def input_courses(num_courses):
    for _ in range(num_courses):
        course_id = input("Enter course ID:")
        course_name = input("Enter course name:")
        course = {"id": course_id, "name": course_name}
        courses.append(course)
    print(f"{num_courses} courses added successfully!")

def input_marks_for_course(course_id):
    # Get the course by course_id
    course = None
    for c in courses:
        if c["id"] == course_id:
            course = c
            break
    if not course:
        print("Course not found!")
        return
    
    print(f"Input marks for course: {course['name']}")
    for student in students:
        mark = float(input(f"Enter marks for student {student['name']} (ID: {student['id']}): "))
        student["marks"][course_id] = mark
    print("Marks entered successfully!")

def list_courses():
    if not courses:
        print("No courses available.")
        return
    print("\nList of Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

def list_students():
    if not students:
        print("No students available.")
        return
    print("\nList of Students:")
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks(course_id):
    course = None
    for c in courses:
        if c["id"] == course_id:
            course = c
            break
    if not course:
        print("Course not found!")
        return
    
    print(f"\nMarks for Course: {course['name']}")
    for student in students:
        marks = student["marks"].get(course_id, None)
        if marks is not None:
            print(f"Student {student['name']} (ID: {student['id']}) - Marks: {marks}")
        else:
            print(f"Student {student['name']} (ID: {student['id']}) - No marks entered.")

# Menu for interacting with the system
def main():
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
            input_students(num_students)

        elif choice == "2":
            num_courses = int(input("Enter number of courses: "))
            input_courses(num_courses)

        elif choice == "3":
            list_courses()
            course_id = input("Enter course ID to input marks: ")
            input_marks_for_course(course_id)

        elif choice == "4":
            list_courses()

        elif choice == "5":
            list_students()

        elif choice == "6":
            list_courses()
            course_id = input("Enter course ID to view marks: ")
            show_student_marks(course_id)

        elif choice == "7":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
