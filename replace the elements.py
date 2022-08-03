num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

n= int(input())
list_new=[]
for i in num_list:
    list_a=list(i)
    list_a[len(list_a)-1]=n
    tuple_a= tuple(list_a)
    list_new += [tuple_a]
    
print(list_new)