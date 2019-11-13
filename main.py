from src.University import University


def main():
    BASE_URL = "./data/stevens_data/"

    stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)
    stevens_university.print_records()

    # table = stevens_university.instructor_table_db("./data/SSW_810")
    # print(table)


main()
