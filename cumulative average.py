N=int(input())
cumulative_sum=0
for inputs in range(1,N+1):
    a=int(input())
    cumulative_sum +=a
    print(round(cumulative_sum/inputs,3))