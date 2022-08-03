def count(arg_1):
    uppercase=0
    lowercase=0
    for char in arg_1:
        var= char.isupper()
        if var:
            uppercase= uppercase+1
        else:
            lowercase= lowercase+1

    print(uppercase)
    print(lowercase)

word= input()
count(word)