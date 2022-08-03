a= int(input())
b= int(input())
even_count=0
odd_count=0
for i in range(a, b+1):
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1
print(even_count)
print(odd_count)