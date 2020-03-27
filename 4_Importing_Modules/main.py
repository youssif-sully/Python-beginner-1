###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       Importing modules                     #
#       main.py                               #
#                                             #
###############################################

# importing the module
import module_3
# importing the module_2 and 'renaming' it for ease of use
# names should be relevant
import module_2 as mod2

# importing 1 variable and function from (module_1)
# note the second variable CAN'T be accessed.
from module_1 import str_mod_1, functionModule1

print("\n{} {} {}\n".format("-" * 9, "Using . to call an variable in "
                                     "module_3 (import module_3)", "-" * 9))

# by specifying the the name of the module first followed by .
# the content of that module can be accessed
print(module_3.str_mod_3)

print("\n{} {} {}\n".format("-" * 9, "Using mod2. to call an variable in "
                                     "module_2 (import module_2 as mod2)", "-" * 9))

print(mod2.str_mod_2)

print("\n{} {} {}\n".format("-" * 9, "Without . to call an variable and a function in "
                                     "module_1 (from module_1 import str_mod_1, "
                                     "multiplicationTable)", "-" * 9))

# note that if (from import) used, the variable (str_mod_1) and the function
# (multiplicationTable()) are defined in the main.py but NOT the module itself
print(str_mod_1)
functionModule1()

print("\n{} {} {}\n".format("-" * 9, "Error: Using . to call an variable in "
                                     "module_1 because from is used(from module_1 "
                                     "import str_mod_1, multiplicationTable)", "-" * 9))

# ERROR: name 'module_1' is not defined
print(module_1.str_mod_1)
