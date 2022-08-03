n= int(input())
list_n= []

for i in range(n):
    a= input()
    list_n= list_n + [a]

length= len(list_n)
for j in range(length):
    print(list_n[length-j-1])