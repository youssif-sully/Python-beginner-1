###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       Dictionary 4.1                        #
#                                             #
###############################################

dict_new = {'key_1': 'value 1', 'key_2': 'value 1', 'key_3': 'value 1'}

# The setdefault() method returns the value of the item with the specified key.
new_key_1 = dict_new.setdefault('key_3', 'new_value')
print("setdefault() Method with key_3")
print(new_key_1, "\n")

# If the key does not exist, insert the key, with the specified value
new_key_2 = dict_new.setdefault('key_4', 'added_value')
print("setdefault() Method with key_4")
print(new_key_2, "\n")

print("The new dict")
print(dict_new)

# items(), values() and keys() Methods
print("\n{} {} {}\n".format("-" * 9, "items(), values() and keys() Methods", "-" * 9))

print(dict_new.items())  # ---> returns list with two values' tuple
print(dict_new.values())  # ---> returns list
print(dict_new.keys())  # ---> returns list

# For loop and dictionary
print("\n{} {} {}\n".format("-" * 9, "For loop and dictionary", "-" * 9))

print("The keys of the dict_new are:")
for key in dict_new:
    print(key)

print("\nThe keys and values of the dict_new are:")
for key, value in dict_new.items():  # dict_new.item returns ---> key and value ---> see above
    print(key, value)

# Del(), pop(), popitem() and clear() Methods
print("\n{} {} {}\n".format("-" * 9, "Del(), pop(), popitem() and clear() Methods", "-" * 9))

# in general pop used to delete AND returns the value of the deleted item
# and popitem delete the last item AND returns the key and value of the deleted item
# where DELETE is specified which value to delete

del dict_new['key_1']
print("After deleting the key_1 item")
print(dict_new, "\n")

temp_value_1 = dict_new.pop('key_2')
print("The popped item is")
print(temp_value_1, "\n")

print("The second popped item is")
temp_value_2 = dict_new.popitem()
print(temp_value_2, "\n")

print(dict_new.clear())  # ---> clear the entire dictionary

# Initialize an empty dictionary
print("\n{} {} {}\n".format("-" * 9, "Initialize an empty dictionary", "-" * 9))

dict_new_2 = dict()
dict_new_2['key_1'] = 'value 1'
print("initialize an empty dictionary with dict()")
print(dict_new_2)

