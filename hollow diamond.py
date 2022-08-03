N=int(input())
#first row
left_spaces=" "*(N-1)
print(left_spaces+"*")
#print upper half triangle
right_spaces_count=-1
for row in range(1, N):
    
    left_spaces_count=N-row-1
    left_spaces=" "*left_spaces_count
    
    right_spaces_count += 2
    right_spaces=" "*right_spaces_count
    print(left_spaces+"*"+right_spaces+"*")
#Lower triangle
for row in range(1, N-1):
    
    left_spaces_count=row
    left_spaces=" "*row
    
    right_spaces_count -= 2
    right_spaces = " "*right_spaces_count
    
    print(left_spaces+"*"+right_spaces+"*")
#last row
left_spaces=" "*(N-1)
print(left_spaces+"*")