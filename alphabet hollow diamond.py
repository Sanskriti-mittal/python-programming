N=int(input())
#upper triangle
unicode_number=65
right_space_number=0
right_alphabate=""
for i in range(1,N+1):
    left_space_number=N-i
    left_space=" "*(left_space_number)
    alphabate=chr(unicode_number)
    right_space=" "*right_space_number
    print(left_space+alphabate+right_space+right_alphabate)
    right_space_number = 2*i-1
    unicode_number += 1
    right_alphabate=chr(unicode_number)
unicode_number -= 2

#lower triangle
for i in range(1,N-1):
    left_space=" "*i
    left_alphabate=chr(unicode_number)
    right_space=" "*(2*(N-i)-3)
    print(left_space+left_alphabate+right_space+left_alphabate)
    unicode_number -= 1
# last line
print(" "*(N-1)+chr(unicode_number))
    