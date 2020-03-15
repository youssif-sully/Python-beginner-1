###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       classes 1.2 INSTANCE variables 2      #
#       methods and __dict__                  #
#                                             #
###############################################

# INSTANCE variables 2
# instead of assigning variables to each INSTANCE (classes_1.py),
# we can def a INSTANCE variables inside the class


class StudentType2:

    # Initializing INSTANCE variables: self (by convention) act like INSTANCE (student_1)
    def __init__(self, f_name, l_name, courses):
        self.f_name = f_name
        self.l_name = l_name
        self.courses = courses

    # Functions inside the class called INSTANCE regular methods
    # INSTANCE regular methods take an INSTANCE as an argument by default
    def email(self):
        return '{}.{}@aol.com'.format(self.f_name.lower(), self.l_name.lower())


# assigning self --> new_student_1 (assigned automatically), f_name --> 'Youssef', l_name --> 'Sully',
# courses --> ['CompSci', 'Telecom']
new_student_1 = StudentType2('Youssef', 'Sully', ['CompSci', 'Telecom'])
new_student_2 = StudentType2('Sully', 'Youssef', ['Telecom', 'CompSci'])

print(new_student_1.f_name, new_student_1.l_name, new_student_1.courses)
print(new_student_2.f_name, new_student_2.l_name, new_student_2.courses, "\n")

# __dict__ methods shows all the INSTANCES variables as dictionary
print(new_student_1.__dict__)
print(new_student_2.__dict__, "\n")

# to call the method inside the class
print(new_student_1.email())
print(new_student_2.email())
