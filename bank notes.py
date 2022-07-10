A= int(input())
no_of_100_notes= A//100
no_of_50_notes= A % 100 //50
no_of_20_notes= A % 100 % 50 //20
no_of_10_notes= A % 100 % 50 % 20 //10
print("100 Notes: "+str(no_of_100_notes))
print("50 Notes: "+str(no_of_50_notes))
print("20 Notes: "+str(no_of_20_notes))
print("10 Notes: "+str(no_of_10_notes))