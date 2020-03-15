###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       classes 1 INSTANCE variables          #
#                                             #
###############################################

# INSTANCE variables
# class: to initialize the class
# pass: to leave the class empty without pass (error)


class StudentType1:
    pass


# assigning the class StudentType1 to a "Variable" and by doing that that Variable called INSTANCE
student_1 = StudentType1()

# f_name, l_name, courses and email called INSTANCE variables
student_1.f_name = 'Youssef'
student_1.l_name = 'Sully'
student_1.courses = ['CompSci', 'Telecom']
student_1.email = 'youssef.sully@aol.com'

# student_2 called INSTANCE
student_2 = StudentType1()

# f_name, 2_name, courses and email called INSTANCE variables
student_2.f_name = 'Sully'
student_2.l_name = 'Youssef'
student_2.courses = ['Telecom', 'CompSci']
student_2.email = 'sully.youssef@aol.com'

# <__main__.StudentType1 object at 0x00AE0FB8>  ---> student_1 is an object located in 0x00AE0FB8 in memory
print(student_1)
# <__main__.StudentType1 object at 0x0107C028>  ---> student_2 is an object located in 0x0107C028 in memory
print(student_2)

# student_1 and student_2 are different object

print(student_1.f_name, student_1.l_name, student_1.courses, student_1.email)
