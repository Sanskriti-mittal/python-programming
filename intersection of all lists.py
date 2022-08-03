def get_int_list(list_a):
    new_list=[]
    for item in list_a:
        new_item=int(item)
        new_list += [new_item]
    return(new_list)
    
input_1=input().split()
num_list_1=get_int_list(input_1)
set_a=set(num_list_1)

input_2=input().split()
num_list_2=get_int_list(input_2)
set_b=set(num_list_2)

input_3=input().split()
num_list_3=get_int_list(input_3)
set_c=set(num_list_3)
result = set_a & set_b & set_c
print(list(result))