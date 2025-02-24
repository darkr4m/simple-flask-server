"""
CLASS Student
ATTRIBUTES:
    students - dict - holds a dictionary of all students (id: Student)
    _id - int - unique - set internally - counts max id in current dict and assigns next number
    _first_name - string - the student's first name
    _last_name - string - the student's last name
    _age - int - the student's age
    _grade - string - A/B/C/D/F - max 1 char

GETTERS AND SETTERS:
    GET id
    GET first_name
    SET first_name
        Must be a string, alpha, no numbers or special characters, greater than 3 chars
    GET last_name
    SET last_name
        Must be a string, alpha, no numbers or special characters, greater than 3 chars
    GET age
    GET grade
    SET grade
        One character string, must be A, B, C, D, F, format - upper

METHODS:
    #get_all_students - class method
        return a list of all Student objects
    
    #get_student_by_id - class method
        Input id
        return a single Student object 

"""

class Student():
    students = {}

    def __init__(self):
        pass