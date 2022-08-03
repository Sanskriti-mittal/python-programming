N=input()
list_a=N.split()
new_list=[]
for item in list_a:
    b=item[0]
    new_list=new_list+[b]
new_list=".".join(new_list)
print(new_list)