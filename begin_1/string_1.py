###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       String 1                              #
#                                             #
###############################################

text_1 = 'Hello there'
# 'JOHN'S CAR' is NOT allowed
# 'JOHN\'S CAR' is allowed \ is a escape sign
text_2 = "JOHN'S CAR"
text_3 = """The this a text with multiple 
lines and uses triple quotation """
text_4 = "      8 whitespaces front"
text_5 = "readme.txt"
text_6 = "0123456789"

print("text_1 is {}".format(text_1))
print("text_2 is {}".format(text_2))
print("text_3 is {}".format(text_3))
print("text_4 is {}".format(text_4))
print("text_5 is {}".format(text_5))

# String index, len and adding
print("\n{} {} {}\n".format("-" * 9, "String index, len and adding", "-" * 9))

new_text = text_1 + " " + text_2
print("text_1 + text_2 = {}".format(new_text))
print("The first letter in text_1 is: {}".format(text_1[0]))
print("The last letter in text_1 is: {}".format(text_1[-1]))
print("The first five letters in text_1 is: {}".format(text_1[0:5]))
print("The last five letters in text_1 is: {}".format(text_1[6:]))
print("The number of character in text_1 is: {}".format(len(text_1)))


# lower(), upper() and count() Methods
print("\n{} {} {}\n".format("-" * 9, "lower(), upper(), count() and find() Methods", "-" * 9))

# upper() changes all characters to uppercase
print("text_1 all uppercase: {}".format(text_1.upper()))

# lower() changes all characters to lowercase
print("text_2 all lowercase: {}".format(text_2.lower()))

# count() returns the how many times the argument occur in the string
print("# of the word Hello in text_1 is: {}".format(text_1.count('Hello')))  # in this case 'Hello' is the argument
print("# of the letter e in text_1 is: {}".format(text_1.count('e')))
print("# of the letter z in text_1 is: {}".format(text_1.count('z')))

# find() returns the position of the argument in the string
print("The position of the letter t in text_1 is: {}".format(text_1.find('t')))

# replace() replaces the OLD argument with new argument
print("Replacing there with John in text_1: {}".format(text_1.replace('there', 'John')))


