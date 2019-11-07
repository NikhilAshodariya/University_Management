from src.University import University


def main():
    BASE_URL = "./data/stevens_data/"

    stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)
    stevens_university.print_records()


main()
