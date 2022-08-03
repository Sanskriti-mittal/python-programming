n= input().split(",")
n= sorted(n)
length_n= len(n)
list_n=[]
for i in range(length_n):
    n[i]= int(n[i])
    list_n += [n[i]]
print(int(n[-1]))