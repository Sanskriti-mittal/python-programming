num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
n= int(input())
new_list= []
for i in range(len(num_list)):
    if num_list[i] > n:
        new_list = new_list + [num_list[i]]
print(new_list)