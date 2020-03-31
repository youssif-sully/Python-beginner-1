###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       File handling 2                       #
#                                             #
###############################################

with open('to_read.txt', 'r') as opened_file:
    text_block = 12

    print(opened_file.read(text_block), end='')
    print("File CURRENT position {}\n".format(opened_file.tell()))

    print(opened_file.read(text_block), end='')
    print("File CURRENT position {}\n".format(opened_file.tell()))

    opened_file.seek(52)
    print("File CURRENT position set to {} using seek()".format(opened_file.tell()))
    print(opened_file.read(text_block))

