def get_int_list(list_a):
    num_list=[]
    for item in list_a:
        new_item=int(item)
        num_list += [new_item]
    return(num_list)

N=int(input())
b=input().split()
result_1=get_int_list(b)
set_b=set(result_1)
common_element=set_b
for i in range(N-1):
    set_a=set()
    a=input().split()
    result=get_int_list(a)
    set_a=set(result)
    common_element= common_element & set_a
list_final=list(common_element)
list_final.sort()
print(list_final)
    
    