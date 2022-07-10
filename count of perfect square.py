A=int(input())
B=int(input())
count=0
for value in range(B+1):
    a=value**2
    if A<=a<=B:
        count=count+1
print(count)