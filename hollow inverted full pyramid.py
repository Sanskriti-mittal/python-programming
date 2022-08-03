r = int(input())
for i in range(r):
    if i==0:
        num=""
        for j in range(1, r+1):
            num= num + str(j) + " "
        print(num)
    elif i==r-1:
        print( " "*(r-1) + "1" + " "*(r-1))
    else:
        print(" "*(i) + "1" + " "*(2*r-2*i-3) + str(r-i))