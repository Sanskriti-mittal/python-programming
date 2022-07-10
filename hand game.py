Abhinav=input()
Anjali=input()
if Abhinav==Anjali:
    print("Tie")
if Abhinav=="Rock":
    if Anjali=="Paper":
        print("Anjali Wins")
    else:
        print("Abhinav Wins")
if Abhinav=="Scissors":
    if Anjali=="Rock":
        print("Anjali Wins")
    else:
        print("Abhinav Wins")
if Abhinav=="Paper":
    if Anjali=="Scissors":
        print("Anjali Wins")
    else:
        print("Abhinav Wins")
