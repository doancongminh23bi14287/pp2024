
def get_number_of_students():
    return int(input("Enter number of students: "))

def get_student_details():
    student_id = input("Enter student ID: ")
    name = input("Enter student's name: ")
    dob = input("Enter student's Date of Birth (DD/MM/YYYY): ")
    return student_id, name, dob

def get_number_of_courses():
    return int(input("Enter number of courses: "))

def get_course_details():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    return course_id, course_name, credits

def get_marks_for_student(student_name, student_id):
    try:
        mark = float(input(f"Enter marks for student {student_name} (ID: {student_id}): "))
        return mark
    except ValueError:
        print("Invalid mark entered. Please enter a number.")
        return None

