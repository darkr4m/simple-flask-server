from flask import Blueprint, jsonify

bp = Blueprint('students',__name__)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

@bp.route('/students')
def all_students():
    # Returns an array of all student objects available.
    return jsonify(students)

@bp.route('/old_students')
def all_students():
    # Returns an array of student objects where the students are older than 20 years old.
    return jsonify(students)

@bp.route('/young_students')
def all_students():
    # Returns an array of student objects where the students are younger than 21 years old.
    return jsonify(students)

@bp.route('/advance_students')
def all_students():
    # Returns an array of student objects where the students are younger than 21 and have a letter grade of "A."
    return jsonify(students)

@bp.route('/student_names')
# Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
def all_students():
    return jsonify(students)

@bp.route('/student_ages')
# Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
def all_students():
    return jsonify(students)
