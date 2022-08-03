a= int(input())
b= int(input())
if a>b:
    smallest_num=b
else:
    smallest_num=a
gcd= 1
for i in range(1, smallest_num+1):
    if (a%i==0) and (b%i==0):
        value=i
        gcd= gcd*value
print(gcd)