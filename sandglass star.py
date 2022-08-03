N=int(input())
# upper triangle
for i in range(N-1):
    stars="* "*(N-i)
    left_space=" "*i
    print(left_space+stars)
#lower triangle
for i in range(1,N+1):
    left_space=" "*(N-i)
    stars="* "*(i)
    print(left_space+stars)