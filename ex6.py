import os
import pickle
import zipfile

def save_data_to_pickle(students, courses, marks, archive="students.dat"):
    # Serialize data to a pickle file
    with open("data.pkl", "wb") as file:
        pickle.dump({"students": students, "courses": courses, "marks": marks}, file)
    # Compress the pickle file into a .dat archive
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("data.pkl")
    os.remove("data.pkl")  # Remove the temporary pickle file
    print(f"Data compressed and saved to {archive}")

def load_data_from_pickle(archive="students.dat"):
    if not os.path.exists(archive):
        print(f"{archive} not found. Starting fresh.")
        return [], [], []

    print(f"{archive} found. Decompressing and loading data...")
    with zipfile.ZipFile(archive, "r") as zipf:
        zipf.extract("data.pkl")  # Extract the pickle file

    # Load data from the pickle file
    with open("data.pkl", "rb") as file:
        data = pickle.load(file)
    os.remove("data.pkl")  # Remove the temporary pickle file
    print("Data successfully loaded.")
    return data["students"], data["courses"], data["marks"]

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

# Main program
students, courses, marks = load_data_from_pickle()

# Input students
num_students = get_number_of_students()
for _ in range(num_students):
    student_id, name, dob = get_student_details()
    students.append({"id": student_id, "name": name, "dob": dob})

# Input courses
num_courses = get_number_of_courses()
for _ in range(num_courses):
    course_id, course_name, credits = get_course_details()
    courses.append({"id": course_id, "name": course_name, "credits": credits})

# Input marks
for student in students:
    for course in courses:
        mark = None
        while mark is None:  # Repeat until valid mark is entered
            mark = get_marks_for_student(student["name"], student["id"])
        marks.append({"student_id": student["id"], "student_name": student["name"], "course_id": course["id"], "mark": mark})

# Save all data into a compressed pickle archive
save_data_to_pickle(students, courses, marks)

print("Data has been successfully saved and compressed.")
