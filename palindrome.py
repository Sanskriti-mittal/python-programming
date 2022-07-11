N=input()
lower_case= N.lower()
counter=len(N)-1
str_new=""
for value in range(len(N)):
    str_new=str_new+str(N[counter-value])
lower_new = str_new.lower()
if lower_new==lower_case:
    print("Palindrome")
else:
    print("Not a Palindrome")