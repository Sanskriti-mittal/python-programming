n= input()
list_n= n.split()
length= len(list_n)
a= int(list_n[0])
new_list=[]
for item in range(1, length):
    b= int(list_n[item])
    if a<b:
        a=b
print(a)