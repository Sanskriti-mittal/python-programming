A=int(input())
B=int(input())
new_string=""
for i in range(A,B+1):
    string=str(i)
    length=len(string)
    sumation=0
    for j in range(length):
        a=string[j]
        sumation += int(a)**length
    if sumation==i:
        new_string += str(i)+" "
if new_string=="":
    print("-1")
else:
    print(new_string)