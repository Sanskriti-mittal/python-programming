a= int(input())
for i in range(1, a+1):
    num= ""
    for v in range(1, a-i+2):
        num = num + str(v) + " "
    print(num)
