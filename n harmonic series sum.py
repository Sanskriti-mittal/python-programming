N=int(input())
series_sum=0
for number in range(1, N+1):
    series_sum += 1/number
print(round(series_sum, 2))