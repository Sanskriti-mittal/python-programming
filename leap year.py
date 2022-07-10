Y = int(input())
is_multiple_of_100 = (Y%100 == 0)
if is_multiple_of_100:
    is_multiple_of_400 = (Y%400 == 0)
    if is_multiple_of_400:
        print("True")
    else:
        print("False")
else:
    is_multiple_of_4 = (Y%4 == 0)
    if is_multiple_of_4:
        print("True")
    else:
        print("False")