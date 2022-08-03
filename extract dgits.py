N=input()
list_a=[]
for i in range(len(N)):
    if N[i].isdigit():
        list_a += [int(N[i])]
sumation=sum(list_a)
minimum=min(list_a)
maximum=max(list_a)
print(sumation)
print(minimum)
print(maximum)