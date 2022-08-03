N=int(input())
A=input()
list_create=A.split()
new_list=[]
for i in range(len(list_create)):
    a=int(list_create[i])
    new_list=new_list+[a]
length=len(new_list)
if length%2 != 0:
    index=int((length+1)/2)
else:
    index=int(length/2)
print(new_list[index: ])