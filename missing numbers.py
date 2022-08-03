def get_integer_list(list_a):
    new_list=[]
    for item in list_a:
        new_item=int(item)
        new_list += [new_item]
    return(new_list)

N=input().split()
integer_list=get_integer_list(N)
maximum=max(integer_list)
new_result=[]
for i in range(1,maximum):
    if i not in integer_list:
        new_result += [i]
print(new_result)