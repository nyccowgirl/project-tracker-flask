"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright
# import pdb

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_grades = hackbright.get_grades_by_github(github)

    return render_template('student_info.html',
                           first=first,
                           last=last,
                           github=github,
                           projects=project_grades)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/new_student")
def display_form():
    """Show form for adding a student."""

    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def make_new_student():
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    github = request.form.get("github")

    first_name, last_name, github = hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_confirm.html", first=first_name,
                           last=last_name, github=github)


@app.route("/project")
def get_project():
    """Show information about a project."""

    project = request.args.get('project')

    title, description, max_grade = hackbright.get_project_by_title(project)

    return render_template('project_info.html',
                           title=title,
                           description=description,
                           max_grade=max_grade)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
