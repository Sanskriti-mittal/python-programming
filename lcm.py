a= int(input())
b= int(input())
if a>b:
    greatest_num=a
    smallest_num =b
else:
    greatest_num=b
    smallest_num=a
lcm= False
for i in range(greatest_num, a*b+1):
    if not lcm:
        if (i % smallest_num==0) and (i % greatest_num==0):
            lcm= True
            value=i
print(value)