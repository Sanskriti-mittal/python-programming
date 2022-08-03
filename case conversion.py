N=input()
count=0
for char in N:
    if char.isupper():
        count += 1
indexing=0
snake_case=""
for i in range(count):
    string=N[indexing]
    count_second=0
    for j in range(indexing+1,len(N)):
        is_upper=N[j].isupper()
        if is_upper:
            break
        string += N[j]
        count_second += 1
    string=string.lower()
    snake_case += string+"_"
    indexing += count_second+1

list_snake_case=list(snake_case)
list_snake_case.pop()
string="".join(list_snake_case)
print(string)
    
    
    
    
    
    
    
    

    

    