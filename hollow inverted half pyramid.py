N=int(input())
first_row=""
for i in range(1, N+1):
    first_row=first_row+str(i)+" "
print(first_row)
for j in range(1, N-1):
    string=""
    for k in range(1, j+1):
        string=" "*(2*(N-k)-3)+str(N-j)
    print("1"+string)
print("1")

#alternate sol
'''
n = int(input())
for row in range(1, n+1):
    i = n - (row - 1)
    if (i > 2) and (i < n):
        hollow_spaces = "  " * (i - 2)
        numbers = "1 " + hollow_spaces + (str(i) + " ")
        print(numbers)
    else:
    numbers = ""
    for j in range(1, i+1):
        numbers = numbers + str(j) + " "
    print(numbers)

'''