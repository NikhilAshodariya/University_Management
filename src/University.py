from prettytable import PrettyTable

from src.Instructor import Instructor
from src.Major import Major
from src.MiscellaneousFunctions import file_reading_gen, is_path_valid
from src.Student import Student
import os
import sqlite3


class University:
    def __init__(self, u_id, name, base_url):
        self.BASE_URL = base_url
        self.university_id = u_id
        self.university_name = name

        self._student_list = {}
        self._prof_list = {}
        self._major = {}

        self.populate_data()

    def __generate_file_urls(self):
        base_url = self.BASE_URL
        if not is_path_valid(base_url):
            raise FileNotFoundError(f"Invalid path {base_url}")

        grades_file = os.path.join(base_url, "grades.txt")
        instructors_file = os.path.join(base_url, "instructors.txt")
        students_file = os.path.join(base_url, "students.txt")
        majors_file = os.path.join(base_url, "majors.txt")

        return grades_file, instructors_file, students_file, majors_file

    def __read_student_instructor_and_grade_file(self):
        # base_url = self.BASE_URL
        grades_file, instructors_file, students_file, majors_file = self.__generate_file_urls()

        majors_data = file_reading_gen(majors_file, 3, "\t", header=True)
        student_data = file_reading_gen(students_file, 3, "\t", header=True)
        instructors_data = file_reading_gen(instructors_file, 3, "\t", header=True)
        grades_data = file_reading_gen(grades_file, 4, "\t", header=True)

        return student_data, instructors_data, grades_data, majors_data

    def add_student(self, student):
        if student.student_details["student_id"] in self._student_list:
            raise ValueError(f"Student exists with id =  {student.student_id}")
        else:
            self._student_list[student.student_details["student_id"]] = student

    def add_professor(self, prof):
        if prof.instructor_details["instructor_id"] in self._prof_list:
            raise ValueError(f"Prof exists with the id = {prof.instructor_id}")
        else:
            self._prof_list[prof.instructor_details["instructor_id"]] = prof

    def get_student_from_id(self, s_id):
        if s_id in self._student_list:
            return self._student_list[s_id]
        else:
            raise ValueError(f"student with id {s_id} does not exists")

    def get_prof_from_id(self, p_id):
        if p_id in self._prof_list:
            return self._prof_list[p_id]
        else:
            raise ValueError(f"Professor with id {p_id} does not exists")

    def _print_major_data_in_table(self):
        x = PrettyTable()
        x.field_names = Major.get_header()

        for val in self._major:
            x.add_row([self._major[val].major, self._major[val].get_required_course(),
                       self._major[val].get_elective_course()])
        return x

    def _print_student_data_in_table(self):
        def set_diff(s1, s2):
            if s1.isdisjoint(s2):
                return s1
            else:
                return None

        x = PrettyTable()

        x.field_names = Student.student_header()

        for val in self._student_list:
            temp = sorted(list(self._student_list[val].student_details["student_courses_taken"].keys()))
            x.add_row([self._student_list[val].student_details["student_id"],
                       self._student_list[val].student_details["student_name"],
                       temp,
                       set(
                           self._major[self._student_list[val].student_details["student_major"]].get_required_course()
                       ) - set(temp),
                       set_diff(set(
                           self._major[self._student_list[val].student_details["student_major"]].get_elective_course()
                       ), set(temp))
                       ]
                      )
        return x

    def _print_prof_data_in_table(self):
        x = PrettyTable()

        x.field_names = ["CWID", "Name", "Dept", "Course", "Students"]

        for val in self._prof_list:
            for inner_val in list(dict(self._prof_list[val].instructor_details["instructor_courses"]).keys()):
                x.add_row([self._prof_list[val].instructor_details["instructor_id"],
                           self._prof_list[val].instructor_details["instructor_name"],
                           self._prof_list[val].instructor_details["instructor_dept_name"],
                           inner_val,
                           dict(self._prof_list[val].instructor_details["instructor_courses"])[inner_val]
                           ])
        return x

    def _connect_to_prof_db(self, db_path):
        db = sqlite3.connect(db_path)
        return db

    def execute_query_on_prof_db(self, query):
        db = self._connect_to_prof_db("../data/SSW_810")
        return db.execute(query)

    def instructor_table_db(self, db_path):
        db = self._connect_to_prof_db(db_path)
        x = PrettyTable()
        x.field_names = ["CWID", "Name", "Dept", "Course", "student_count"]
        query = '''
        select i.cwid, i.Name, i.Dept, g.Course, COUNT(*) as student_count
        from instructors i,
             grades g
        where i.CWID = g.InstructorCWID
        group by i.CWID, g.Course;
        '''
        for row in db.execute(query):
            x.add_row(list(row))
        return x

    def populate_student_data(self, student_data):
        for val in student_data:
            if val[2] not in self._major:
                raise ValueError(f"You have wrong major in the file supplied major = {val[2]}")
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

    def populate_major_data(self, majors_data):
        # self._major
        for index, val in enumerate(majors_data):
            if val[0] not in self._major:
                self._major[val[0]] = Major(val[0])

            major_obj = self._major[val[0]]
            if val[1] == 'R' or val[1] == 'r':
                major_obj.add_required_course(val[2])
            elif val[1] == "E" or val[1] == 'e':
                major_obj.add_elective_course(val[2])
            else:
                raise ValueError(f"value at index {index} for major's data is wrong val = {val[1]}")

    def populate_data(self):
        student_data, instructors_data, grades_data, majors_data = self.__read_student_instructor_and_grade_file()

        try:
            self.populate_major_data(majors_data)
            self.populate_student_data(student_data)
            self.populate_instructor_data(instructors_data)
            self.populate_grade_data(grades_data)
        except Exception as e:
            print(f"Internal error {e}")

    def print_records(self):
        print(self._print_major_data_in_table())
        print(self._print_prof_data_in_table())
        print(self._print_student_data_in_table())
        print(self.instructor_table_db("./data/SSW_810"))

    def student_list_getter(self):
        return self._student_list

    def prof_list_getter(self):
        return self._prof_list

    def major_list_getter(self):
        return self._major
