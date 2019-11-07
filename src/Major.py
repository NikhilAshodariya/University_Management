class Major:
    def __init__(self, major):
        self._major = major
        self._required_course = []
        self._elective_course = []

    @staticmethod
    def get_header():
        return ["Dept", "Required", "Electives"]

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    def add_required_course(self, course_name):
        self._required_course.append(course_name)

    def add_elective_course(self, course_name):
        self._elective_course.append(course_name)

    def get_required_course(self):
        return self._required_course[:]

    def get_elective_course(self):
        return self._elective_course[:]
