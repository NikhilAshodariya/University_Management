import unittest

from src.Instructor import Instructor


class TestInstructor(unittest.TestCase):

    def test_add_courses_thought(self):
        instructor = Instructor(1234, "XYZ", "CS")
        instructor.add_courses_thought("CS321", 3)
        print(instructor.instructor_details)
        self.assertEqual(instructor.instructor_details, {'instructor_id': 1234,
                                                         'instructor_name': 'XYZ',
                                                         'instructor_dept_name': 'CS',
                                                         'instructor_courses': {'CS321': 3}
                                                         }
                         )


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
