import unittest

from src.Student import Student


class TestStudent(unittest.TestCase):
    def test_add_course(self):
        st = Student(1234, "ABC", "CS")
        st.add_course("CS120", "A")
        self.assertEqual(st.student_details, {
            'student_id': 1234,
            'student_name': 'ABC',
            'student_major': 'CS',
            'student_courses_taken': {
                'CS120': 'A'
            }
        })


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
