N=input()
count_of_G=0
count_of_R=0
for char in N:
    if char=="G":
        count_of_G += 1
    else:
        count_of_R += 1

if count_of_R>count_of_G:
    count_required=count_of_G
else:
    count_required=count_of_R
print(count_required)