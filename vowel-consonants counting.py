N=input().split()
new_upper_var=""
for i in range(len(N)):
    N[i]=N[i].upper()
    new_upper_var+=N[i]
    
count_vowel=0
count_consonent=0
for char in new_upper_var:
    if char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
        count_vowel += 1
    else:
        count_consonent +=1
print(count_vowel)
print(count_consonent)
