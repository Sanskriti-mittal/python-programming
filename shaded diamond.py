N=int(input())
#upper part
for row in range(N):
    print(" "*(N-1-row)+"* "*(row+1))
#lower part except last row
hollow_spaces_count=2*(N-2)-1
for row in range(1,N-1):
    left_spaces=" "*row
    hollow_spaces= " "*hollow_spaces_count
    print(left_spaces+"*"+hollow_spaces+"*")
    hollow_spaces_count -= 2
#last row
print(" "*(N-1)+"*")