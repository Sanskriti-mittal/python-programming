r= int(input())
for i in range(1, r+1):
    string_formed= ""
    new_string= ""
    for j in range(1, i+1):
        string_formed= string_formed+ str(j)+ " "
    new_string= (" "*(r-j) + string_formed)
    print(new_string)
