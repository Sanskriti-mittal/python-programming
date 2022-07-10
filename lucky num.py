a=int(input())
b=int(input())
c= a==6 or b==6 or a+b==6 or a-b==6 or b-a==6
if c:
    print("Lucky")
else: 
    print("Not Lucky")