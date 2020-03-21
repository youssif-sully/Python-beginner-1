print("Hello from module_1, contents: 2 variables and a function")

str_mod_1 = 'this a variable in module_1'
int_mod_1 = 13

def multiplicationTable():
    
    for i in range(1, 11):
       print("\n")
       for j in range(1 ,11):
           print("{:02} * {:02} = {:02} |".format(i, j, i * j), end=' ')
           

