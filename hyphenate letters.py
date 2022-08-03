N=input()
new_string=N[0]
for char in N[1:len(N)]:
    new_string= new_string+"-"+char
print(new_string)