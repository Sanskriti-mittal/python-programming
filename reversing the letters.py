n= input()
list_n= n.split()
list_new= []
length_n= len(list_n)
for i in range(length_n):
    new= list_n[i][::-1]
    list_new= list_new + [new]
list_output=[]
list_output= " ".join(list_new)
print(list_output)