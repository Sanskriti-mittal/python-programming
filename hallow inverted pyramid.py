r= int(input())
for i in range(r):
    if i==0:
        print("* "*r)
    elif i== r-1:
        print("*")
    else:
        print("*" + " "*(2*(r-i)-3 )+ "*")