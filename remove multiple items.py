num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
N=input().split()
for item in N:
    a=int(item)  
    num_set.discard(a)
num_list=list(num_set)
num_list.sort()
print(num_list)