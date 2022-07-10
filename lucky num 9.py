a=input()
b=int(a[0])
c=int(a[1])
number_multiple_9= int(a)%9
is_multiple = number_multiple_9 == 0
one_digit_9 = b==9 or c==9
if is_multiple or one_digit_9:
    print("Lucky Number")
else:
    print("Unlucky Number")