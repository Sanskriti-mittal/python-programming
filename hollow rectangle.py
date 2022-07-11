m_row= int(input())
n_col= int(input())
for i in range(m_row):
    if i==0 or i==(m_row-1):
        print("* "*(n_col))
    else:
        print("*"+" "*(2*n_col-3)+"*")