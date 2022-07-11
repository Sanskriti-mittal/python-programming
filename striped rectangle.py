n= int(input())
m= int(input())
count= ""
for i in range(1, n+1):
    if i%2!=0:
        for x in range(m):
            count= count+ str("+")+ " "
        print(count)
        count= ""
    else:
        for x in range(m):
            count= count+ str("-")+ " "
        print(count)
        count= ""
