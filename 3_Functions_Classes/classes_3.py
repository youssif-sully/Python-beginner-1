###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       classes 2 class variables             #
#                                             #
###############################################

# class variables
# unlike the INSTANCE variables class variables are the same for all INSTANCES
# Ex. new_student_1 has f_name = 'Youssef' and new_student_2 has f_name = 'Sully'


class StudentType2:
    # department is a class variables and it's the same for all INSTANCES
    department = 'Software'
    title = 'Student'

    def __init__(self, f_name, l_name, courses):
        self.f_name = f_name
        self.l_name = l_name
        self.courses = courses

    def email(self):
        return '{}.{}@aol.com'.format(self.f_name.lower(), self.l_name.lower())

    def depart(self):
        # class variables called through 1. INSTANCES (self), 2. class (StudentType2)
        # department called through INSTANCE and title called through class
        # see the difference below
        return '{} {}'.format(self.department, StudentType2.title)


new_student_1 = StudentType2('Youssef', 'Sully', ['CompSci', 'Telecom'])
new_student_2 = StudentType2('Sully', 'Youssef', ['Telecom', 'CompSci'])

print(new_student_1.depart())
print(new_student_2.depart(), "\n")

# since title is called through the class changing would change it for the entire class
StudentType2.title = 'Senior student'
print(new_student_1.depart())
print(new_student_2.depart(), "\n")


# 'department': 'Software', 'title': 'Senior student' as attributes of the class StudentType2
print(StudentType2.__dict__, "\n")
# no department and title in the INSTANCES' variables
print(new_student_1.__dict__)
print(new_student_2.__dict__, "\n")


# since department is called through the INSTANCE changing would change it only for that INSTANCE
new_student_1.department = 'Information'
print(new_student_1.depart())
print(new_student_2.depart(), "\n")

# since department was changed (called through INSTANCES in the class see above) in the above line
# it becomes now part of the INSTANCE (new_student_1 only) variables
print(new_student_1.__dict__)
print(new_student_2.__dict__, "\n")