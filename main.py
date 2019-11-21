from flask import render_template

from src.University import University


def main():
    BASE_URL = "./data/stevens_data/"

    stevens_university = University("Stevens_01", "Stevens Institute of Technology", BASE_URL)
    stevens_university.print_records()

    # table = stevens_university.instructor_table_db("./data/SSW_810")
    # print(table)

    from flask import Flask
    app = Flask(__name__)

    @app.route('/instructor_courses')
    def hello_world():
        cursor = stevens_university.get_inst_data("./data/SSW_810")
        return render_template("instructor.html", data=cursor)
        # return 'Hello, World!'

    app.run(debug=True)

main()
