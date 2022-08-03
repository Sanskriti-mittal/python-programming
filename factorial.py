def compute_factorial(n):
    # Complete this recursive function
    if n==1:
        return(1)
    factorial=n*compute_factorial(n-1)
    return(factorial)


num = int(input())
# Call the compute_factorial function
result=compute_factorial(num)
print(result)