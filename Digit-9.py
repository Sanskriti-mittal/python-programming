N=int(input())
for row in range(2*N-1):
    if row==0 or row==N-1 or row==2*N-2:
        print("* "*N)
    elif 0<row<N-1:
        hollow_space_count=2*(N-2)+1
        hollow_space=" "*hollow_space_count
        print("*"+hollow_space+"*")
    else:
        hollow_space_count=2*(N-1)
        hollow_space=" "*hollow_space_count
        print(hollow_space+"*")