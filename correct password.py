a= input()
correct= False
for i in range(len(a)):
    is_digit= a[i].isdigit()
    correct= correct or is_digit
if correct:
    print("Valid Password")
else:
    print("Invalid password")
