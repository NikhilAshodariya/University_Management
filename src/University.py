from prettytable import PrettyTable

from src.Instructor import Instructor
from src.MiscellaneousFunctions import file_reading_gen, is_path_valid
from src.Student import Student
import os


class University:
    def __init__(self, u_id, name, base_url):
        self.BASE_URL = base_url
        self.university_id = u_id
        self.university_name = name

        self.student_list = {}
        self.prof_list = {}

        self.populate_data()

    def __generate_file_urls(self):
        base_url = self.BASE_URL
        if not is_path_valid(base_url):
            raise FileNotFoundError(f"Invalid path {base_url}")

        grades_file = os.path.join(base_url, "grades.txt")
        instructors_file = os.path.join(base_url, "instructors.txt")
        students_file = os.path.join(base_url, "students.txt")

        return grades_file, instructors_file, students_file

    def __read_student_instructor_and_grade_file(self):
        # base_url = self.BASE_URL
        grades_file, instructors_file, students_file = self.__generate_file_urls()

        student_data = file_reading_gen(students_file, 3, "\t")
        instructors_data = file_reading_gen(instructors_file, 3, "\t")
        grades_data = file_reading_gen(grades_file, 4, "\t")

        return student_data, instructors_data, grades_data

    def add_student(self, student):
        if student.student_details["student_id"] in self.student_list:
            raise ValueError(f"Student exists with id =  {student.student_id}")
        else:
            self.student_list[student.student_details["student_id"]] = student

    def add_professor(self, prof):
        if prof.instructor_details["instructor_id"] in self.prof_list:
            raise ValueError(f"Prof exists with the id = {prof.instructor_id}")
        else:
            self.prof_list[prof.instructor_details["instructor_id"]] = prof

    def get_student_from_id(self, s_id):
        if s_id in self.student_list:
            return self.student_list[s_id]
        else:
            raise ValueError(f"student with id {s_id} does not exists")

    def get_prof_from_id(self, p_id):
        if p_id in self.prof_list:
            return self.prof_list[p_id]
        else:
            raise ValueError(f"Professor with id {p_id} does not exists")

    def print_student_data_in_table(self):
        x = PrettyTable()

        x.field_names = ["CWID", "Name", "Completed Courses"]

        for val in self.student_list:
            x.add_row([self.student_list[val].student_details["student_id"],
                       self.student_list[val].student_details["student_name"],
                       sorted(list(self.student_list[val].student_details["student_courses_taken"].keys()))
                       ]
                      )
        return x

    def print_prof_data_in_table(self):
        x = PrettyTable()

        x.field_names = ["CWID", "Name", "Dept", "Course", "Students"]

        for val in self.prof_list:
            for inner_val in list(dict(self.prof_list[val].instructor_details["instructor_courses"]).keys()):
                x.add_row([self.prof_list[val].instructor_details["instructor_id"],
                           self.prof_list[val].instructor_details["instructor_name"],
                           self.prof_list[val].instructor_details["instructor_dept_name"],
                           inner_val,
                           dict(self.prof_list[val].instructor_details["instructor_courses"])[inner_val]
                           ])
        return x

    def populate_student_data(self, student_data):
        for val in student_data:
            st = Student(val[0], val[1], val[2])
            self.add_student(st)

    def populate_instructor_data(self, instructors_data):
        for val in instructors_data:
            temp = Instructor(val[0], val[1], val[2])
            self.add_professor(temp)

    def populate_grade_data(self, grades_data):
        for val in grades_data:
            student = self.get_student_from_id(val[0])
            student.add_course(val[1], val[2])

            prof = self.get_prof_from_id(val[-1])
            prof.add_courses_thought(val[1])

    def populate_data(self):
        student_data, instructors_data, grades_data = self.__read_student_instructor_and_grade_file()

        self.populate_student_data(student_data)
        self.populate_instructor_data(instructors_data)
        self.populate_grade_data(grades_data)
