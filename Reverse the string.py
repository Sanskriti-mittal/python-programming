N=input()
counter=len(N)-1
string_new=""
for value in range(len(N)):
    string_new=string_new+N[counter-value]
print(string_new)