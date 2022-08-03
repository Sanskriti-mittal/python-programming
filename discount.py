def get_discount(amount):
    # Complete this function
    if amount<500:
        result="5%"
    elif amount<2500:
        result="10%"
    else:
        result="20%"
    print(result)
amount = int(input())
# Call the get_discount function
get_discount(amount)