M=int(input())
no_of_2000_notes=M//2000
no_of_500_notes=M % 2000 // 500
no_of_200_notes=M % 2000 % 500 // 200
no_of_50_notes=M % 2000 % 500 % 200//50
no_of_20_notes=M % 2000 % 500 % 200 % 50//20
no_of_5_notes= M % 2000 % 500 % 200 % 50 % 20//5
no_of_2_notes= M % 2000 % 500 % 200 % 50 % 20 % 5//2
no_of_1_notes= M % 2000 % 500 % 200 % 50 % 20 % 5 % 2//1
print("2000:"+str(no_of_2000_notes)+" 500:"+str(no_of_500_notes)+" 200:"+str(no_of_200_notes)+" 50:"+str(no_of_50_notes)+" 20:"+str(no_of_20_notes)+" 5:"+str(no_of_5_notes)+" 2:"+str(no_of_2_notes)+" 1:"+str(no_of_1_notes))
