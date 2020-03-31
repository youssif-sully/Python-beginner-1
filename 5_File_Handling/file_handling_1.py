###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       File handling 1                       #
#                                             #
###############################################

# from https://docs.python.org/3/library/functions.html#open
# 'r' open for reading(default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode(default)
# '+' open for updating(reading and writing)

# Not recommended implementation (close() the resources (Ex. files and Network ports) is imperative
# and in case any error before file.close() the resource (file) will be still open)
file = open('to_read.txt', 'r')
print("\nUsing open (without context manager) to open the {}".format(file.name))
file.close()

print("\n{} {} {}\n".format("-" * 9, "Using context manager with read() method", "-" * 9))

# using context manager is recommended (Note: file.close() is NOT included because
# it is done automatically)
with open('to_read.txt', 'r') as opened_file:
    print(opened_file.read())  # read() used for small files (because it loads all the contents
    # into memory)

print("\n{} {} {}\n".format("-" * 9, "Using context manager with read() 2 method", "-" * 9))

with open('to_read.txt', 'r') as opened_file:
    print(opened_file.read(20), end='')  # read(50) returns the first 50 characters
    print(opened_file.read(70))  # read(100) returns the NEXT 100 characters, if there are no characters returns
    # empty string

print("\n{} {} {}\n".format("-" * 9, "Using context manager processing blocks using while "
                                     "loop and read() method", "-" * 9))

with open('to_read.txt', 'r') as opened_file:
    text_block = 5  # reading chunks
    file_contents = opened_file.read(text_block)  # assigning to file_contents
    while len(file_contents) > 0:  # first run len(file_contents) == 5
        print(file_contents, end='<>')  # adds <> every 5 char
        file_contents = opened_file.read(text_block)  # next chunk of text (next 5 char)
    print("\n")

print("\n{} {} {}\n".format("-" * 9, "Using context manager with readlines() method", "-" * 9))

with open('to_read.txt', 'r') as opened_file:
    print(opened_file.readlines())  # readlines() returns a list

print("\n{} {} {}\n".format("-" * 9, "Using context manager with readline() method", "-" * 9))

with open('to_read.txt', 'r') as opened_file:
    print(opened_file.readline(), end='')  # readline() returns the CURRENT line
    print(opened_file.readline(), end='')

print("\n{} {} {}\n".format("-" * 9, "Using context manager with for loop", "-" * 9))

with open('to_read.txt', 'r') as opened_file:
    for line in opened_file:
        print(line, end='')
