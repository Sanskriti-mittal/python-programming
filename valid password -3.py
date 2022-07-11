N=input()
atleast_digit=False
atleast_upper=False
atleast_lower=False
for value in range(len(N)):
    is_digit=N[value].isdigit()
    atleast_digit=atleast_digit or is_digit
    is_upper=N[value].isupper()
    atleast_upper=atleast_upper or is_upper
    is_lower=N[value].islower()
    atleast_lower=atleast_lower or is_lower
if atleast_lower and atleast_upper and atleast_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    