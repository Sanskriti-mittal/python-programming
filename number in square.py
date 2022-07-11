a= int(input())
count= ""
for i in range(a):
    for value in range(1,a+1):
        count= count+str(value)+" "
    print(count)
    count=""
