operator = input()
a=int(input())
b=int(input())
if operator=="+":
    print(a+b)
elif operator=="-":
    if a>b:
        print(a-b)
    else:
        print(b-a)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
elif operator=="%":
    print(a%b)