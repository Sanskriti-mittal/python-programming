a= input()
first_digit = int(a[0])
second_digit = int(a[1])
third_digit = int(a[2])
sum_of_cube_of_all_digit = first_digit ** 3 + second_digit ** 3 + third_digit ** 3
if int(a)==sum_of_cube_of_all_digit:
    print("True")
else:
    print("False")