M=int(input())
N=int(input())
if not(M>1):
    M=2
a=0
for i in range(M,N+1):
    factor=0
    for j in range(2,i):
        if i%j==0:
            factor=factor+1
    if factor==0:
        a=i
        print(a)
        break
if a==0:
    print("No prime numbers in the given range")