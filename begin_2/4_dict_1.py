###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       Dictionary 1                          #
#                                             #
###############################################

dict_info_1 = {'first_name': 'Youssef',
               'last_name': 'Sully',
               'age': 33,
               'courses': ['Telecom theory', 'Informatics']}

# first_name ---> Youssef
# first_name is the KEY and it represent the value Youssef

print("\n{} {} {}\n".format("-" * 9, "Dictionary output", "-" * 9))

print("My first name is {} ".format(dict_info_1['first_name']))
print("My last name is {} ".format(dict_info_1['last_name']))
print("My age is {} ".format(dict_info_1['age']))

# to access a list inside a dictionary we have to specify the index of that list
print("My courses are in {} and {} ".
      format(dict_info_1['courses'][0],
             dict_info_1['courses'][1]))

# print(dict_info_1[0])
# ---> error because dictionary represented NOT by index rather by KEYS


# get() Method
print("\n{} {} {}\n".format("-" * 9, "get() Method", "-" * 9))

# get('KEY', 'message if the KEY is NOT EXIST') Method
print(dict_info_1.get('first_name'))

# in case there is no KEY (name), output message 'NOT EXIST'
print(dict_info_1.get('name', 'NOT FOUND'))

# Adding and updating values
print("\n{} {} {}\n".format("-" * 9, "Adding and updating values", "-" * 9))

dict_info_1['first_name'] = 'Youssif'
dict_info_1['middle_name'] = 'M.'
print("Updating value: Youssef ---> Youssif")
print("Adding new KEY and VALUE: ---> 'middle_name': 'M.'")
print(dict_info_1, "\n")

print("Updating VALUES: SULLY ---> Solli and 33 ---> 43")
dict_info_1.update({'last_name': 'Solli',
                    'age': 43})
print(dict_info_1)

# copy() Method"
print("\n{} {} {}\n".format("-" * 9, "copy() Method", "-" * 9))

dict_info_2 = dict_info_1.copy()
print("The new dict is a copy of the previous one")
print(dict_info_2)

# fromkeys() , zip() and setdefault() Methods
print("\n{} {} {}\n".format("-" * 9, "fromkeys() , zip() and setdefault() Methods", "-" * 9))

# zip () maps two lists into a dictionary
keys = ['Color 1', 'Color 2', 'Color 3']
values = ['red', 'green', 'blue']
color_dictionary = dict(zip(keys, values))
print("The zip() method maps two lists into a dictionary")
print(color_dictionary, "\n")

tuple_1 = ('key_1', 'key_2', 'key_3')
values = 'some random value'

dict_new = dict.fromkeys(tuple_1, values)
print(dict_new, "\n")