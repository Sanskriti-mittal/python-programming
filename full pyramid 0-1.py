r= int(input())
for i in range(1, r+1):
    print("0 "*(r-i) + "1 "*(2*i-1) + "0 "*(r-i))