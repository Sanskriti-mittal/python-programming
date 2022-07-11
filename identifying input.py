n= input()
is_digit= n.isdigit()
is_uppercase= n.isupper()
is_lowercase= n.islower()
if is_digit:
    print("Digit")
if is_uppercase:
    print("Uppercase Letter")
if is_lowercase:
    print("Lowecase Letter")
else:
    print("Special character")