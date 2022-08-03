N=int(input())
M=int(input())
factor=0
for i in range(1,N+1):
        if N%(N+1-i)==0:
            Mth_largest_factor=N+1-i
            factor=factor+1
            if factor==M:
                break
print(Mth_largest_factor)