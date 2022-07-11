a= input()
upper_case= ""
new_word= ""
for i in range(len(a)):
    if a[i].islower():
        upper_case= a[i].upper()
        new_word= new_word + upper_case
    else:
        lower_case= a[i].lower()
        new_word= new_word + lower_case
print(new_word)

     