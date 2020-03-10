###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       While Loops                           #
#                                             #
###############################################


# 1. in while loop we have to INITIALIZE the variable (iterator = 0)
# 2. execute the below command until this statement is (iterator < 10) TRUE

print("\n{} {} {}\n".format("-" * 9, "While loop", "-" * 9))

iterator = 0
while iterator < 10:
    print("{} ".format(iterator), end='')
    # means the new iterator = old iterator + 1 ---> the new value of the iterator is 1
    # # also can be written as ---> iterator += 1
    iterator = iterator + 1

print("\n")
print("{} {} {}\n".format("-" * 9, "Using break", "-" * 9))

# break used to break out of the loop
iterator = 0
while iterator < 10:
    if iterator == 4:
        print("Number 4 is reached the loop stopped due to break")
        break
    print("{} ".format(iterator), end='')
    iterator += 1

print("\n{} {} {}\n".format("-" * 9, "Infinite loop", "-" * 9))

# Infinite loop needs a BREAK condition otherwise is going to run forever!
iterator = 0
while True:
    if iterator == 4:
        print("Number 4 is reached the loop stopped due to break")
        break
    print("{} ".format(iterator), end='')
    iterator += 1
