a = input()
b = input()
part_a=int (a[0:(len(a)-1)])
if part_a>=75:
    print("Allowed to write exam")
if part_a<75 and b=="Y":
    print("Allowed to write exam")
if part_a<75 and b=="N":
    print("Cannot write exam")