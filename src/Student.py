class Student:

    @staticmethod
    def student_header():
        return ["CWID", "Name", "Completed Courses", "Remaining Course", "Remaining Electives"]

    def __init__(self, cwid, name, major_name):
        self._student_details = {
            "student_id": cwid,
            "student_name": name,
            "student_major": major_name,
            "student_courses_taken": {

            }
        }

    @property
    def student_details(self):
        return self._student_details

    @student_details.setter
    def student_details(self, val):
        raise ValueError("You cannot modify the value of student_details")

    def add_course(self, course_name, grade):
        if grade.upper() in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
            self.student_details["student_courses_taken"][course_name] = grade.upper()
