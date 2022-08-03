N=input()
list_a=N.split()
sum_of=0
for item in list_a:
    sum_of=sum_of+int(item)
average=sum_of/len(list_a)
print(round(average, 2))