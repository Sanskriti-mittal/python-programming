a= int(input())
b= int(input())
for i in range(a, b+1):
    factor=0
    for v in range(2,i):
        if i%v==0:
            factor= factor+1
    if factor==0:
        print(i)