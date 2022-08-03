n= int(input())

list_n= []
for i in range(n):
    a= input()
    if i<3 or i>=n-3:
        list_n= list_n + [a]
print(list_n)