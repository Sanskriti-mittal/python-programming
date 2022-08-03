N=int(input())
set_divisible_by_2=set()
for i in range(1,2*N+1):
    if i%2==0:
        set_divisible_by_2= set_divisible_by_2 | {i}
    else:
        continue
set_divisible_by_3=set()
for i in range(1,3*N+1):
    if i%3 == 0:
        set_divisible_by_3= set_divisible_by_3 | {i}
    else:
        continue
multiple_of_two_not_3=set_divisible_by_2 - set_divisible_by_3
list_a=list(multiple_of_two_not_3)
list_a.sort()
print(list_a)
symmetric_diff= set_divisible_by_2 ^ set_divisible_by_3
list_b=list(symmetric_diff)
list_b.sort()
print(list_b)
