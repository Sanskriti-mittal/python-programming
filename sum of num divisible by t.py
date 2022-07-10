n = int(input())
m = int(input())
t = int(input())
sum= 0 
for i in range(n, m+1):
    if i%t == 0:
        sum = sum + i
    else:
        i = i+1
print(sum)