n= int(input())

# for first row
stars= "* "*(2*n)
print(stars)

#for upper diamond
hollow_spaces_count= 0
for i in range(1, n):
    stars= "* "*(n-i)
    hollow_spaces_count= hollow_spaces_count + 4
    hollow_spaces= " "*(hollow_spaces_count)
    print(stars + hollow_spaces + stars)

#for middle part
print("*" + " "*2*(2*n-2) + " *")

#for lower part
for j in range(2,n):
    stars= "* "*(j)
    hollow_spaces_count= hollow_spaces_count - 4
    hollow_spaces= " "*(hollow_spaces_count)
    print(stars + hollow_spaces + stars)

#for last part
stars= "* "*(2*n)
print(stars)