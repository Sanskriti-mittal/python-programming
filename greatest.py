N= int(input())
a = int(input())

for i in range(N-1):
    b = int(input())
    if b>=a:
        a=b
print(a) 