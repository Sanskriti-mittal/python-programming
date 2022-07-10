units= int(input())
if 0<=units<=50:
    bill_amount=units*2
elif 51<=units<=150:
    bill_amount=100+(units-50)*3
elif 151<=units<=250:
    bill_amount=400+(units-150)*5
elif 251<=units:
    bill_amount= 900+(units-250)*8
bill_amount=(bill_amount*120/100)
print(bill_amount)