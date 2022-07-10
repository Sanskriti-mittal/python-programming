A = input()
length = len(A)
if length == 1:
    sum_of_digit = int(A)
elif length == 2:
    sum_of_digit = int(A[0])+int(A[1])
elif length == 3:
    sum_of_digit = int(A[0])+int(A[1])+int(A[2])
elif length == 4:
    sum_of_digit = int(A[0])+int(A[1])+int(A[2])+int(A[3])
elif length == 5:
    sum_of_digit = int(A[0])+int(A[1])+int(A[2])+int(A[3])+int(A[4])
print(sum_of_digit)