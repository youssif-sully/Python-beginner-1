# Created by Youssef

# Formatting

dict_info = {'first_name': 'Youssef', 'last_name': 'Sully', 'age': 33}

print("\n{} {} {}\n".format("-" * 9, "Bad implementation of printing multiple output", "-" * 9))

output = 'My first name is ' + dict_info['first_name'] + dict_info['first_name'] + \
         ' and I am ' + str(dict_info['age']) + ' years old.'
print(output)

print("\n{} {} {}\n".format("-" * 9, "Use of formatting", "-" * 9))

output = 'My name is {} {} and I am {} years old.'.format(dict_info['first_name'],
                                                          dict_info['last_name'], dict_info['age'])
print(output)

print("\n{} {} {}\n".format("-" * 9, "Order formatting 1", "-" * 9))

output = 'My name is {first_name} {last_name} and I am {age} years old.'.format(first_name='Youssef',
                                                                                last_name='Sully', age='30')
print(output)

print("\n{} {} {}\n".format("-" * 9, "Order formatting 2", "-" * 9))

output = 'My name is {0} {2} and I am {1} years old.'.format(dict_info['first_name'],
                                                             dict_info['age'], dict_info['last_name'])
print(output)

print("\n{} {} {}\n".format("-" * 9, "Referencing a dictionary", "-" * 9))

output = 'My name is {first_name} {last_name} and I am {age} years old.'.format(**dict_info)
print(output)

print("\n{} {} {}\n".format("-" * 9, "Direct operation inside the format", "-" * 9))

output = '25 / 5 is equal to {} bytes'.format(25 / 5)
print(output)

print("\n{} {} {}\n".format("-" * 9, "Different variation of int output", "-" * 9))

# using the :03 inside the curly brackets to display three digits instead of 1
integer_number = 3
output = 'The value of the integer_number is {} but after using \n:03 inside the curly ' \
         'brackets it displayed as {:03}'.format(integer_number, integer_number)
print(output, "\n")

# using the :.2f inside the curly brackets to display two digits after the comma!
output = '1 / 3 is equal to {} and in order to display two ' \
         '\ndigits after the comma we use :.2f inside the curly ' \
         'brackets {:.2f}'.format(1 / 3, 1 / 3)
print(output)