N=input().split(",")
M=input().split(",")
list_a=N
new_input_list=[]
for item in list_a:
    a=int(item)
    new_input_list += [a]
set_a=set(new_input_list)

list_b=M
new_input_list_second=[]
for item in list_b:
    b=int(item)
    new_input_list_second += [b]
set_b=set(new_input_list_second)

intersection_set= set_b & set_a
list_intersection=list(intersection_set)
list_intersection.sort()
print(list_intersection)