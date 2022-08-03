def fibonacci(n):
    # Complete this function to return nth term in fibonacci series
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
    
def get_fibonacci_series(n):
    # Complete this function to return list of n terms of fibonacci series
    fibonacci_series_new=[]
    for i in range(n):
        fibonacci_series_new += [fibonacci(i)]
    return fibonacci_series_new
    
n = int(input())
# Call the get_fibonacci_series function
result=get_fibonacci_series(n)
print(result)