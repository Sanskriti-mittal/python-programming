N=int(input())
#first row
print("* "*(2*N-1))
hollow_space_count=0
for i in range(1,N):
    left_spaces=" "*i
    hollow_space=" "*hollow_space_count
    print(left_spaces+"* "*(N-i)+hollow_space+"* "*(N-i))
    hollow_space_count += 2
    