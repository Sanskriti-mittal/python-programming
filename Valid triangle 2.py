a=int(input())
b=int(input())
c=int(input())
size_compare=(a+b>c and b+c>a and c+a>b)
if size_compare:
    print("It's a Triangle")
else:
    print("It's not a Triangle")