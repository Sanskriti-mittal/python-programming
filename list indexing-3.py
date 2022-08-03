n= int(input())
t= int(input())
list_n= []
for i in range(n):
    a= int(input())
    list_n= list_n + [a]
for j in range(t):
    b= int(input())
    print(list_n[b])