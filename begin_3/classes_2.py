###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       classes 2 Class variables             #
#       and methods                           #
#                                             #
###############################################

# Class variables
# instead of assigning variables to each INSTANCE (classes_1.py), we can def a Class variables


class StudentType2:

    # Initializing class variables: self (by convention) act like INSTANCE (student_1)
    def __init__(self, f_name, l_name, courses):
        self.f_name = f_name
        self.l_name = l_name
        self.courses = courses

    # Functions inside the class called methods
    def email(self):
        return '{}.{}@aol.com'.format(self.f_name, self.l_name)


# assigning self --> new_student_1 , f_name --> 'Youssef', l_name --> 'Sully',
# courses --> ['CompSci', 'Telecom']
new_student_1 = StudentType2('Youssef', 'Sully', ['CompSci', 'Telecom'])

print(new_student_1.f_name, new_student_1.l_name, new_student_1.courses)

# to call the method inside the class
print(new_student_1.email())
