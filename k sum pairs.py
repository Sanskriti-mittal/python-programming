def get_int_list(list_a):
    num_list=[]
    for item in list_a:
        new_item=int(item)
        num_list += [new_item]
    return(num_list)
    
N=input().split(",")
num_list=get_int_list(N)

K=int(input())
set_new=set()
for index in range(len(num_list)):
    a=num_list[index]
    b=K-a
    if b in num_list[index+1:]:
        list_b=[a,b]
        list_b.sort()
        tupple_a=tuple(list_b)
        set_new.add(tupple_a)
list_new=list(set_new)
list_new.sort()
for item in list_new:
    print(item)