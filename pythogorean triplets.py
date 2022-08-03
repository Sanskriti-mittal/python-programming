a= int(input())
count=0
for c in range(1, a+1):
    for a in range(1, c):
        for b in range(a):
            if a**2 + b**2 == c**2:
                count= count+1
print(count)
