from unittest import result

list_a= input().split(",")
list_b= input().split(",")
length_of_list_a= len(list_a)
n= length_of_list_a - 1

for i in range(length_of_list_a):
    num_a= list_a[i]
    num_b= list_b[n-i]
    result= str(num_a) + " " + str(num_b)
    print(result)