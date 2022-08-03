N=int(input())
sum_of_non_prime=0
for i in range(N):
    a=int(input())
    count=0
    for j in range(2,a):
        if a%j==0:
            count=count+1
    if count!=0:
        sum_of_non_prime += a
print(sum_of_non_prime)