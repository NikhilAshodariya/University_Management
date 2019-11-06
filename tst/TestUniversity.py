import unittest

from src.University import University


class TestUniversity(unittest.TestCase):
    def test_university(self):
        """This method is a tests the university method of the class"""
        BASE_URL = "../data/tst_data/"

        stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)

        student_table = stevens_university.print_student_data_in_table()
        prof_table = stevens_university.print_prof_data_in_table()


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
