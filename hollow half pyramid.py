r= int(input())
for i in range(1, r+1):
    if (2<i<r):
        num= "1 " + "  "*(i-2) + (str(i) + " ")
        print(num)
    else:
        num=""
        for j in range(1, i+1):
            num= num + (str(j)+" ")
        print(num)
