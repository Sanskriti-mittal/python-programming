num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
input_list=input().split()
num_list=[]
for item in input_list:
    num_item=int(item)
    num_list += [num_item]
set_input=set(num_list)

check_superset=num_set.issuperset(set_input)
if check_superset:
    print("Superset")
check_subset= num_set.issubset(set_input)
if check_subset:
    print("Subset")
check_disjoint=num_set.isdisjoint(set_input)
if check_disjoint:
    print("Disjoint Set")
