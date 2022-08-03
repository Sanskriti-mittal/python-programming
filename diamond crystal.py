N=int(input())
#first row
print(" "*(N-1)+"/\\")
#upper part
for row in range(1,N):
    left_space=" "*(N-row-1)
    hollow_space_count=2*row
    hollow_space=" "*hollow_space_count
    print(left_space+"/"+hollow_space+"\\")
#middle row
#print("\\"+" "*(2*N-2)+"/")
#lower part
for row in range(1,N):
    left_space=" "*(row-1)
    hollow_space=" "*(2*N-2*row)
    print(left_space+"\\"+hollow_space+"/")
#last part
print(" "*(N-1)+"\\/")