M = int(input())
no_of_500_notes = M//500
no_of_50_notes = (M % 500) // 50
no_of_10_notes = (M % 500 % 50)//10
no_of_1_notes = (M % 500 % 50 % 10)//1
print("500: {} 50: {} 10: {} 1: {}".format(no_of_500_notes, no_of_50_notes, no_of_10_notes, no_of_1_notes))