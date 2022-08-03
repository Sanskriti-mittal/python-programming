def square(arg_1):
    list_a= arg_1.split(",")
    length_list_a= len(list_a)
    list_b=[]
    for i in range(length_list_a):
        double= int(list_a[i])**2
        list_b= list_b + [double]
    print(list_b)

a= input()
square(a)