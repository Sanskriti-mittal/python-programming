N=input()
list_a=N.split(",")
for i in range(len(list_a)):
    list_a[i]=int(list_a[i])
list_a=sorted(list_a)
K=int(input())
kth_largest=list_a[-K]
print(kth_largest)