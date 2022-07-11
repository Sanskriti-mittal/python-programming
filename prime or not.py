a= int(input())
factor= 0 
for i in range(2,a):
    if a%i==0:
        factor= factor + 1
    else:
        i=i+1
if factor==0:
    print("Prime number")
else:
    print("Not a prime number")