###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       String 2                              #
#                                             #
###############################################

text_1 = 'Hello there'
text_4 = "      8 whitespaces front"
text_5 = "readme.txt"
text_6 = "0123456789"


# strip(), endswith(), isnumeric(), split() and join()
print("\n{} {} {}\n".format("-" * 9, "strip(), endswith(), isnumeric(), split() and join()", "-" * 9))

# strip() removes the whitespace
print("text_4 after removing the whitespaces: {}".format(text_4.strip()))
print("text_1 with first letter striped: {}".format(text_1.strip('H')))

# endswith() returns TRUE or FALSE
print("is text_5 ends with .txt: {}".format(text_5.endswith('.txt')))

# isnumeric() returns TRUE or FALSE
print("are all the characters of text_6 numbers: {}".format(text_6.isnumeric()))

# split() spilt the string into a LIST based on the argument
print("split text_5 into two items in a list: {}".format(text_5.split('.')))

# join() takes all items in an iterable and joins them into one string.
separator = '/'
print("Joining / with text_1: {}".format(separator.join(text_1)))


print("\n{} {} {}\n".format("-" * 9, "using (in)", "-" * 9))

word_check = 'Hello' in text_1
print("is the word Hello in text_1: {}".format(word_check))