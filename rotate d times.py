def get_int_list(list_a):
    num_list=[]
    for item in list_a:
        new_item=int(item)
        num_list += [new_item]
    return(num_list)    
N=input().split(",")
num_list=get_int_list(N)

D=int(input())
index=D%(len(num_list))
first_part=num_list[:index]
second_part=num_list[index:]
second_part.extend(first_part)
print(second_part)