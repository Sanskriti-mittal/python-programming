r= int(input())
for i in range(1, r+1):
    if i==1:
        print(" "*(r-1) + ("1"))
    elif i==r:
        num= ""
        for v in range(1, r+1):
            num= num + str(v) + " "
        print(num)
    else:
        print(" "*(r-i)+ "1" + " "*(2*i-3)+ str(i))