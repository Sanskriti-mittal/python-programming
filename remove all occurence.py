nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
N=int(input())
count=nums_list.count(N)
for i in range(count):
    nums_list.remove(N)
print(nums_list)