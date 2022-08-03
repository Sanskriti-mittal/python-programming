input_1=input()
strip=float(input_1[0:len(input_1)-1])

if input_1[-1]=="C":
    C=strip
if input_1[-1]=="F":
    C=round((strip-32)*5/9,2)
if input_1[-1]=="K":
    C=strip-273
print("{}C".format(C))
F=C*9/5+32
F=round(F,1)
print("{}F".format(F))
K=C+273
K=round(K,2)
print("{}K".format(K))