N=int(input())
list_a=[]
for i in range(N):
    a=input()
    input_list=a.split()
    if input_list[0]=="append":
        b=int(input_list[1])
        list_a.append(b)
        
    if input_list[0]=="insert":
        b=int(input_list[1])
        c=int(input_list[2])
        list_a.insert(b,c)
        
    if input_list[0]=="sort":
        list_a.sort()
        
    if input_list[0]=="print":
        print(list_a)
        
    if input_list[0]=="remove":
        b=input_list[1]
        list_a.remove(int(b))
        
    if input_list[0]=="pop":
        list_a.pop()