N=int(input())
years=N//365

weeks=(N%365)//7

days=((N%365)%7)

print("{} years {} weeks {} days".format(years,weeks,days))