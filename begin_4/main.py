# importing the module
import module_3
# importing the module_2 and 'renaming' it for ease of use
# names should be relevent
import module_2 as mod2

# importing 1 variable and function from (module_1)
# note the second variable CAN'T be accessed.
from module_1 import str_mod_1, multiplicationTable

# by specifying the the name of the module first followed by .
# the content of that module can be accessed 
print("\n")
print(module_3.str_mod_3)
print(mod2.str_mod_2)

# note that if (from import) used, the variable (str_mod_1) and the function 
# (multiplicationTable()) are defined in the main.py but NOT the module itself
print(str_mod_1)
print(multiplicationTable())

# ERROR: name 'module_1' is not defined
print(module_1.str_mod_1)