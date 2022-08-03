input_list= input().split()
input_list_new=[]
for item in input_list:
    item= int(item)
    input_list_new += [item]
input_list_new.sort()
a=input_list_new[0]
new_list=[a]
for j in range(1,len(input_list_new)):
    if input_list_new[j]==a:
        continue
    else:
        new_list=new_list+[input_list_new[j]]
        a=input_list_new[j]
print(new_list)