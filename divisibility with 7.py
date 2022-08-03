from unittest import result


def divisible_by_seven(arg_1):
    if arg_1%7==0:
        result= True
    else:
        result= False
    print(result)

n= int(input())
divisible_by_seven(n)
