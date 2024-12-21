import math

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10

    def calculate_gpa(self, course_credits):
        total_credits = sum(course_credits.values())
        weighted_sum = sum(self.marks[course_id] * course_credits[course_id] for course_id in self.marks if course_id in course_credits)
        return weighted_sum / total_credits if total_credits > 0 else 0
