a= input()
b=int(a[0])
c=int(a[1])
sum_of_digit = b+c
one_digit_7 = (b==7) or (c==7)
number_multiple_7 = (int(a)%7) ==0
if (sum_of_digit==7) or one_digit_7 or number_multiple_7:
    print("Special Number")
else:
    print("Normal Number")