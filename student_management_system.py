import os
import zipfile

def decompress_and_load_data(archive="students.dat"):
    if not os.path.exists(archive):
        print(f"{archive} not found. Starting fresh.")
        return [], [], []

    print(f"{archive} found. Decompressing and loading data...")
    with zipfile.ZipFile(archive, "r") as zipf:
        zipf.extractall()  # Extract all files in the archive

    # Load data from decompressed files
    students = []
    courses = []
    marks = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, dob = line.strip().split(", ")
                students.append({"id": student_id, "name": name, "dob": dob})
    except FileNotFoundError:
        print("students.txt not found. Skipping student data.")

    try:
        with open("courses.txt", "r") as file:
            for line in file:
                course_id, course_name, credits = line.strip().split(", ")
                courses.append({"id": course_id, "name": course_name, "credits": int(credits)})
    except FileNotFoundError:
        print("courses.txt not found. Skipping course data.")

    try:
        with open("marks.txt", "r") as file:
            for line in file:
                student_id, student_name, course_id, mark = line.strip().split(", ")
                marks.append({"student_id": student_id, "student_name": student_name, "course_id": course_id, "mark": float(mark)})
    except FileNotFoundError:
        print("marks.txt not found. Skipping marks data.")

    print("Data successfully loaded from the archive.")
    return students, courses, marks

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

def write_students_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student['id']}, {student['name']}, {student['dob']}\n")

def write_courses_to_file(courses, filename="courses.txt"):
    with open(filename, "w") as file:
        for course in courses:
            file.write(f"{course['id']}, {course['name']}, {course['credits']}\n")

def write_marks_to_file(marks, filename="marks.txt"):
    with open(filename, "w") as file:
        for mark in marks:
            file.write(f"{mark['student_id']}, {mark['student_name']}, {mark['course_id']}, {mark['mark']}\n")

def compress_files_to_dat(output_file="students.dat", *files):
    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file)
    print(f"Files compressed into {output_file}")

# Main program
students, courses, marks = decompress_and_load_data()

# Input students
num_students = get_number_of_students()
for _ in range(num_students):
    student_id, name, dob = get_student_details()
    students.append({"id": student_id, "name": name, "dob": dob})
write_students_to_file(students)

# Input courses
num_courses = get_number_of_courses()
for _ in range(num_courses):
    course_id, course_name, credits = get_course_details()
    courses.append({"id": course_id, "name": course_name, "credits": credits})
write_courses_to_file(courses)

# Input marks
for student in students:
    for course in courses:
        mark = None
        while mark is None:  # Repeat until valid mark is entered
            mark = get_marks_for_student(student["name"], student["id"])
        marks.append({"student_id": student["id"], "student_name": student["name"], "course_id": course["id"], "mark": mark})
write_marks_to_file(marks)

# Compress all files into a single archive
compress_files_to_dat("students.dat", "students.txt", "courses.txt", "marks.txt")

print("Data has been successfully written to files and compressed.")
