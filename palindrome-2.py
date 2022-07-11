a= input()
reverse= ""
count= len(a)-1
for i in range(len(a)):
    reverse= reverse+(a[count-i])
reverse= reverse.upper()
a= a.upper()
if a==reverse:
    print("True")
else:
    print("False")