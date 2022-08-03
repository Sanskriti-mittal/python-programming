def str_to_int(n):
    list_n=[]
    for item in n:
        list_n += [int(item)]
    return(list_n)

n= input().split()
list_n= str_to_int(n)
print(list_n)