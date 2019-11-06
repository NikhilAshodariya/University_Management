from src.University import University


def main():
    BASE_URL = "./data/stevens_data/"

    stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)

    student_table = stevens_university.print_student_data_in_table()
    prof_table = stevens_university.print_prof_data_in_table()

    print(student_table)
    print(prof_table)


main()
