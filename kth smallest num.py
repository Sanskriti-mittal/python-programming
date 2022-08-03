list_a=input().split(",")
K=int(input())
for i in range(len(list_a)):
    list_a[i]=int(list_a[i])

list_a=sorted(list_a, reverse=True)


kth_smallest_number=list_a[-K]
print(kth_smallest_number)