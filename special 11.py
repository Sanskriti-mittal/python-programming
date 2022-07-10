a=input()
multiple_11 = int(a)%11
if_multiple = multiple_11==0
if_one_more= multiple_11==1
if if_multiple or if_one_more:
    print("Special Eleven")
else:
    print("Normal Number")