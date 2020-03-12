###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       Dictionary 1                          #
#                                             #
###############################################

dict_info_1 = {'first_name': 'Youssef', 'last_name': 'Sully', 'age': 33, 
               'degree': ['Telecom eng.', 'Informatics']}
# first_name ---> Youssef
# first_name is the KEY and it represent the value Youssef

print("\n{} {} {}\n".format("-" * 9, "Dictionary output", "-" * 9))

print("My first name is {} ".format(dict_info_1['first_name']))
print("My last name is {} ".format(dict_info_1['last_name']))
print("My age is {} ".format(dict_info_1['age']))

# to access a list inside a dictionary we have to specify the index of that list
print("My degrees are in {} and {} ".
      format(dict_info_1['degree'][0],
             dict_info_1['degree'][1]))

# print(dict_info_1[0])
# ---> error because dictionary represented NOT by index rather by KEYS

print("\n{} {} {}\n".format("-" * 9, "get() Method", "-" * 9))

# get('KEY', 'message if the KEY is NOT EXIST') Method
print("Printing the value of the first name using get() method".
      format(dict_info_1.get('first_name')))

# in case there is no KEY (name), output message 'NOT EXIST'
print("in case there is no KEY (name), output message 'NOT EXIST' {}".
      format(dict_info_1.get('name', 'NOT EXIST')))

print("\n{} {} {}\n".format("-" * 9, "Adding and updating values", "-" * 9))

dict_info_1['first_name'] = 'Youssif'
dict_info_1['middle_name'] = 'M.'
print(dict_info_1)

dict_info_1.update({'last_name': 'Solli',
                    'age': 43})
print(dict_info_1)

print("\n{} {} {}\n".format("-" * 9, "copy() Method", "-" * 9))

dict_info_2 = dict_info_1.copy()
print(dict_info_2)

print("\n{} {} {}\n".format("-" * 9, "fromkeys() and setdefault() Methods", "-" * 9))

tuple_1 = ('key_1', 'key_2', 'key_3')
values = 'value'

dict_new = dict.fromkeys(tuple_1, values)
print(dict_new)

# The setdefault() method returns the value of the item with the specified key.
new_key_1 = dict_new.setdefault('key_3', 'new_value')
print(new_key_1)

# If the key does not exist, insert the key, with the specified value
new_key_2 = dict_new.setdefault('key_4', 'added_value')
print(new_key_2)

print(dict_new)

print("\n{} {} {}\n".format("-" * 9, "items(), values() and keys() Methods", "-" * 9))

print(dict_info_1.items())  # ---> returns list with two values' tuple
print(dict_info_1.values())  # ---> returns list
print(dict_info_1.keys())  # ---> returns list

print("\n{} {} {}\n".format("-" * 9, "Del(), pop(), popitem() and clear() Methods", "-" * 9))

# in general pop used to delete AND returns the value of the deleted item
# and popitem delete the last item AND returns the key and value of the deleted item
# where DELETE is specified which value to delete 

del dict_info_1['last_name']
print(dict_info_1)

temp_value_1 = dict_info_1.pop('first_name')
print(temp_value_1)

temp_value_2 = dict_info_1.popitem()
print(temp_value_2)

print(dict_info_1.clear())  # ---> clear the entire dictionary
