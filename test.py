import operator

class Student:
    def __init__(self, name, age, marks, roll_number):
        self.name = name
        self.age = age
        self.marks = marks
        self.roll_number = roll_number

def sort_by(students, criterias):
    new_students = students
    for criteria in criterias:
        new_students = sorted(students, key=operator.attrgetter(criteria))

    return new_students


if __name__ == "__main__":
    stud_obj1 = Student("sk1", "29", "90", "1234")
    stud_obj2 = Student("sk2", "22", "90", "1235")
    stud_obj3 = Student("sk3", "20", "90", "1236")
    stud_obj4 = Student("sk4", "25", "90", "1237")

    students = [stud_obj1, stud_obj2, stud_obj3, stud_obj4]   # list of objects
    criterias = ["age", 'name'] #list of criterias
    sorted_students = sort_by(students, criterias)
    for s in sorted_students :print(s.name)
    print(sorted_students)

