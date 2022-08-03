N=int(input())

for row in range(2,N+2):
    number_line=""
    for column in range(1,row):
        number_line=number_line+str(column)+" "
    print(" "*(N+1-row)+number_line)
    
for row in range(2, N+1):
    number_line=""
    for column in range(1, N+2-row):
        number_line=number_line+str(column)+" "
    print(" "*(row-1)+number_line)
    