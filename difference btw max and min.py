list_a=input().split(",")
for i in range(len(list_a)):
    list_a[i]=int(list_a[i])
largest=max(list_a)
smallest=min(list_a)
print(largest-smallest)