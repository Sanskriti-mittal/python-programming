r= int(input())
for i in range(1, r+1):
    string= ""
    output= ""
    for j in range(1, i+1):
        string= string + str(j)
        if j>1:
            output= output + str(i+1-j)
    print(string+output)
    