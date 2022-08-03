def message(arg_1, arg_2):
    output= arg_1 + " is " + str(arg_2) + " years old."
    return(output)

name= input()
age= int(input())
output= message(name,age)
print(output)