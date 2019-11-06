from collections import defaultdict


class Instructor:
    def __init__(self, i_id, name, dept_name):
        self.instructor_details = {
            "instructor_id": i_id,
            "instructor_name": name,
            "instructor_dept_name": dept_name,
            "instructor_courses": defaultdict(int)
        }

    def add_courses_thought(self, course_name, no_of_student=1):
        self.instructor_details["instructor_courses"][course_name] += no_of_student
