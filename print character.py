from operator import length_hint


n= input()
length_of_n= len(n)
counter=0
while counter< length_of_n:
    print(n[counter])
    counter= counter+1
