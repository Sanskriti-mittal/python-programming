N=input()
atleast_oneupper=False
for value in range(len(N)):
    is_upper=N[value].isupper()
    atleast_oneupper=atleast_oneupper or is_upper
if atleast_oneupper:
    print("Valid Password")
else:
    print("Invalid Password")