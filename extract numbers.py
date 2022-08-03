def get_int(list_a):
    num_list=[]
    for item in list_a:
        is_digit= item.isdigit()
        if is_digit:
            num_list_item=int(item)
            num_list += [num_list_item]
    return(num_list)
    
N=input().split(",")
result=get_int(N)
print(result)