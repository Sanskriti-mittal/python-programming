a= int(input())
count= ""
new=1
for i in range(a):
    for v in range(1,a+1):
        count= count+str(new) + " "
    print(count)
    count=""
    new= new+1