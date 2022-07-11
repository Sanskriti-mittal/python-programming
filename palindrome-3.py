N=input()
N=N.replace(" ","")
N=N.replace(",","")
N=N.replace("'","")
reverse=""
counter=len(N)-1
for value in range(len(N)):
    reverse=reverse+N[counter-value]
reverse=reverse.upper()
N=N.upper()
if N==reverse:
    print("True")
else:
    print("False")