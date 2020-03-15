###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       For Loops 2                           #
#                                             #
###############################################

# a list
number_list = [1, 2, 3, 4, 5]

# for loop with:
# 1. (number) is the iterator
# 2. the initial value of the iterator (number) is the first element in the number_list (1)
#    and the last value is the last element in the number_list (10)

for number in number_list:
    print("{} ".format(number), end='')

print("\n{} {} {}\n".format("-" * 9, "Using break", "-" * 9))

# break used to break out of the loop
for number in number_list:
    if number == 2:
        print("Number 2 is reached the loop stopped due to break")
        break
    print(number)

print("\n{} {} {}\n".format("-" * 9, "Using continue", "-" * 9))

# continue used to continue the loop
for number in number_list:
    if number == 2:
        print("Number 2 is reached the loop continued due to continue")
        continue  # continue the loop and NOT execute print(number)
    print(number)

print("\n{} {} {}\n".format("-" * 9, "Double loop", "-" * 9))

# double_loop
for number in number_list:
    for character in 'xyz':
        print("{}{} ".format(number, character), end='')

print("\n{} {} {}\n".format("-" * 9, "Range", "-" * 9))

# Range
for i in range(1, 11, 2):  # 1 is the initial value, 11 is the end value and 2 is the step
    print("{} ".format(i), end='')
