r= int(input())
for i in range(r):
    row_out = " " * (r-i-1)
    row_out = row_out + "$" * r
    print(row_out)