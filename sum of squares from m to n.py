def squares_addition(arg_1, arg_2):
    square_sum=0
    for i in range(arg_1, arg_2+1):
        square_sum= square_sum + i*i
    return(square_sum)

m= int(input())
n= int(input())
result= squares_addition(m,n)
print(result)