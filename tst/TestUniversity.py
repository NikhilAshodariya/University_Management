import unittest

from src.University import University


class TestUniversity(unittest.TestCase):
    def test_prof_list(self):
        def test_prof(actual_prof, expected_prof):
            self.assertEqual(actual_prof["instructor_id"], expected_prof["instructor_id"])
            self.assertEqual(actual_prof["instructor_name"], expected_prof["instructor_name"])
            self.assertEqual(actual_prof["instructor_dept_name"], expected_prof["instructor_dept_name"])
            self.assertEqual(actual_prof["instructor_courses"], expected_prof["instructor_courses"])

        BASE_URL = "../data/tst_data/"

        stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)
        prof_list = stevens_university.prof_list_getter()

        prof_98764 = prof_list["98764"].instructor_details
        prof_98763 = prof_list["98763"].instructor_details
        prof_98762 = prof_list["98762"].instructor_details

        expected_prof_98764 = {'instructor_id': '98764', 'instructor_name': 'Cohen, R',
                               'instructor_dept_name': 'SFEN',
                               'instructor_courses': {'CS 546': 1}}

        expected_prof_98763 = {'instructor_id': '98763', 'instructor_name': 'Rowland, J', 'instructor_dept_name': 'SFEN',
                               'instructor_courses': {'SSW 810': 4, 'SSW 555': 1}}

        expected_prof_98762 = {'instructor_id': '98762', 'instructor_name': 'Hawking, S',
                               'instructor_dept_name': 'CS', 'instructor_courses': {'CS 501': 1, 'CS 546': 1, 'CS 570': 1}}

        test_prof(prof_98762, expected_prof_98762)
        test_prof(prof_98763, expected_prof_98763)
        test_prof(prof_98764, expected_prof_98764)

    def test_verify_prof_data(self):
        # instructor_table_db
        BASE_URL = "../data/tst_data/"

        query = '''
        select i.cwid, i.Name, i.Dept, g.Course, COUNT(*) as student_count
        from instructors i,
             grades g
        where i.CWID = g.InstructorCWID
        group by i.CWID, g.Course;
        '''

        stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)
        cursor = stevens_university.execute_query_on_prof_db(query)
        db_prof_list = []
        for row in cursor:
            db_prof_list.append(row)

    def test_student_list(self):
        """This method is a tests the university method of the class"""

        def test_student(actual_std, expected_std):
            self.assertEqual(actual_std["student_id"], expected_std["student_id"])
            self.assertEqual(actual_std["student_name"], expected_std["student_name"])
            self.assertEqual(actual_std["student_major"], expected_std["student_major"])
            self.assertEqual(actual_std["student_courses_taken"], expected_std["student_courses_taken"])

        BASE_URL = "../data/tst_data/"

        stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)
        std_list = stevens_university.student_list_getter()

        student_10103 = std_list["10103"].student_details
        student_10115 = std_list["10115"].student_details
        student_10183 = std_list["10183"].student_details
        student_11714 = std_list["11714"].student_details

        expected_student_10103 = {'student_id': '10103', 'student_name': 'Jobs, S', 'student_major': 'SFEN',
                                  'student_courses_taken': {'CS 501': 'B', 'SSW 810': 'A-'}}

        expected_student_10115 = {'student_id': '10115', 'student_name': 'Bezos, J', 'student_major': 'SFEN',
                                  'student_courses_taken': {'SSW 810': 'A'}}

        expected_student_10183 = {'student_id': '10183', 'student_name': 'Musk, E', 'student_major': 'SFEN',
                                  'student_courses_taken': {'SSW 555': 'A', 'SSW 810': 'A'}}

        expected_student_11714 = {'student_id': '11714', 'student_name': 'Gates, B', 'student_major': 'CS',
                                  'student_courses_taken': {'CS 546': 'A', 'CS 570': 'A-', 'SSW 810': 'B-'}}

        test_student(student_10103, expected_student_10103)
        test_student(student_10115, expected_student_10115)
        test_student(student_10183, expected_student_10183)
        test_student(student_11714, expected_student_11714)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
