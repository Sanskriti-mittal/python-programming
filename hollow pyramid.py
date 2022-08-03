r= int(input())
for i in range(r):
    if i==0:
        print("* ")
    elif i==r-1:
        print("* "*r)
    else:
        print("* "+ " "*(2*i-2) +"*")