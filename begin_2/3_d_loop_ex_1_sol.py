###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       double loop example 1 solution        #
#       using for and while loops             #
#                                             #
###############################################

# Method 1
for i in range(1, 10):
    print(i)
    if i == 4:
        j = 1
        while j != 11:
            print('{} '.format(j), end='')
            j += 1

# Method 2
print("\n")
for i in range(1, 10):
    print(i)
    if i == 4:
        for j in range(1, 11):
            print('{} '.format(j), end='')

# Method 3
print("\n")
i = 1
while i != 10:
    print(i)
    i += 1
    if i == 5:
        for j in range(1, 11):
            print('{} '.format(j), end='')




