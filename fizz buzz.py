def fizz_buzz(number):
    # Complete this function
    if number<0:
        number=-number
    else:
        number=number

    if number%3 == 0 and number%5 != 0:
        result="Fizz"
    if number%5 == 0 and number%3 != 0:
        result="Buzz"
    if number%3 == 0 and number%5 == 0:
        result="FizzBuzz"
    if number%3 != 0 and number%5 != 0:
        result=number
    return(result)
number = int(input())
# Call the fizz_buzz function
result=fizz_buzz(number)
print(result)
