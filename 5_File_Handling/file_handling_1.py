# 'r' read, 'w' write, 'a' append and 'r+' read and write

# Not recommended implementation (close() the resources (Ex. files and Network ports) is imperative
# and in case any error before file.close() the resource (file) will be still open)
file = open('test.txt', 'r')
print("\nUsing open (without context manager) to open the {}".format(file.name))
file.close()

print("\n{} {} {}\n".format("-" * 9, "Using context manager with read() method", "-" * 9))

# using context manager is recommended (Note: file.close() is NOT included because
# it is done automatically)
with open('test.txt', 'r') as opened_file:
    print(opened_file.read())  # read() used for small files (because it loads all the contents
    # into memory)

print("\n{} {} {}\n".format("-" * 9, "Using context manager with read() 2 method", "-" * 9))

with open('test.txt', 'r') as opened_file:
    print(opened_file.read(50), end='')  # read(50) returns the first 50 characters
    print(opened_file.read(100))  # read(100) returns the NEXT 100 characters, if there are no characters returns
    # empty string

print("\n{} {} {}\n".format("-" * 9, "Using context manager processing blocks using while "
                                     "loop and read() method", "-" * 9))

with open('test.txt', 'r') as opened_file:
    text_block = 10  # reading chunks
    file_contents = opened_file.read(text_block)  # assigning to file_contents
    while len(file_contents) > 0:  # first run len(file_contents) == 10
        print(file_contents, end='<>')  # adds <> every 10 char
        file_contents = opened_file.read(text_block)  # next chunk of text (next 10 char)
    print("\n")

print("\n{} {} {}\n".format("-" * 9, "Using context manager with readlines() method", "-" * 9))

with open('test.txt', 'r') as opened_file:
    print(opened_file.readlines())  # readlines() returns a list

print("\n{} {} {}\n".format("-" * 9, "Using context manager with readline() method", "-" * 9))

with open('test.txt', 'r') as opened_file:
    print(opened_file.readline(), end='')  # readline() returns the CURRENT line
    print(opened_file.readline(), end='')

print("\n{} {} {}\n".format("-" * 9, "Using context manager with for loop", "-" * 9))

with open('test.txt', 'r') as opened_file:
    for line in opened_file:
        print(line, end='')
