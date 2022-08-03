N=int(input())
K=int(input())
new_var=N+int(K*(K+1)/2)-1
for row in range(2,K+2):
    string=""
    for i in range(1, row):
        string=string+str(new_var)+" "
        new_var -= 1
    print(string)