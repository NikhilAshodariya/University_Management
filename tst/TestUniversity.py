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

        prof_98765 = prof_list["98765"].instructor_details
        prof_98764 = prof_list["98764"].instructor_details
        prof_98763 = prof_list["98763"].instructor_details
        prof_98762 = prof_list["98762"].instructor_details
        prof_98761 = prof_list["98761"].instructor_details
        prof_98760 = prof_list["98760"].instructor_details

        expected_prof_98765 = {'instructor_id': '98765', 'instructor_name': 'Einstein, A',
                               'instructor_dept_name': 'SFEN', 'instructor_courses': {'SSW 567': 4, 'SSW 540': 1}}

        expected_prof_98764 = {'instructor_id': '98764', 'instructor_name': 'Feynman, R',
                               'instructor_dept_name': 'SFEN',
                               'instructor_courses': {'SSW 564': 3, 'SSW 687': 3, 'CS 501': 1, 'CS 545': 1}}

        expected_prof_98763 = {'instructor_id': '98763', 'instructor_name': 'Newton, I', 'instructor_dept_name': 'SFEN',
                               'instructor_courses': {'SSW 555': 1}}

        expected_prof_98762 = {'instructor_id': '98762', 'instructor_name': 'Hawking, S',
                               'instructor_dept_name': 'SYEN', 'instructor_courses': {}}

        expected_prof_98761 = {'instructor_id': '98761', 'instructor_name': 'Edison, A', 'instructor_dept_name': 'SYEN',
                               'instructor_courses': {}}

        expected_prof_98760 = {'instructor_id': '98760', 'instructor_name': 'Darwin, C', 'instructor_dept_name': 'SYEN',
                               'instructor_courses': {}}

        test_prof(prof_98760, expected_prof_98760)
        test_prof(prof_98761, expected_prof_98761)
        test_prof(prof_98762, expected_prof_98762)
        test_prof(prof_98763, expected_prof_98763)
        test_prof(prof_98764, expected_prof_98764)
        test_prof(prof_98765, expected_prof_98765)

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
        student_10172 = std_list["10172"].student_details
        student_10175 = std_list["10175"].student_details
        student_11658 = std_list["11658"].student_details

        expected_student_10103 = {'student_id': '10103', 'student_name': 'Baldwin, C', 'student_major': 'SFEN',
                                  'student_courses_taken': {'SSW 567': 'A', 'SSW 564': 'A-', 'SSW 687': 'B',
                                                            'CS 501': 'B'}}

        expected_student_10115 = {'student_id': '10115', 'student_name': 'Wyatt, X', 'student_major': 'SFEN',
                                  'student_courses_taken': {'SSW 567': 'A', 'SSW 564': 'B+', 'SSW 687': 'A',
                                                            'CS 545': 'A'}}

        expected_student_10172 = {'student_id': '10172', 'student_name': 'Forbes, I', 'student_major': 'SFEN',
                                  'student_courses_taken': {'SSW 555': 'A', 'SSW 567': 'A-'}}

        expected_student_10175 = {'student_id': '10175', 'student_name': 'Erickson, D', 'student_major': 'SFEN',
                                  'student_courses_taken': {'SSW 567': 'A', 'SSW 564': 'A', 'SSW 687': 'B-'}}

        expected_student_11658 = {'student_id': '11658', 'student_name': 'Kelly, P', 'student_major': 'SYEN',
                                  'student_courses_taken': {}}

        test_student(student_10103, expected_student_10103)
        test_student(student_10115, expected_student_10115)
        test_student(student_10172, expected_student_10172)
        test_student(student_10175, expected_student_10175)
        test_student(student_11658, expected_student_11658)

    if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)
