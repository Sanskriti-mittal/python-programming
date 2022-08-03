N=int(input())
b=int(input())
print(str(b))
for i in range(1,N):
    a=int(input())
    if a>b:
        b=a
    print(str(b))