list_a = input().split(",")
#list of string now convert it into list of numbers
list_b=[]
for item in list_a:
    list_b=list_b+[int(item)]

#sort the items in list
list_c= sorted(list_b)

#squaring
list_x = []
for num in list_c:
    list_x += [int(num)**2]
print(list_x)