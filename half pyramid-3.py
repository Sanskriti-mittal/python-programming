starting_number=int(input())
rows=int(input())
for row in range(2, rows+2):
    string=""
    for i in range(1, row):
        string=string+str(starting_number)+" "
        starting_number += 1
    print(string)