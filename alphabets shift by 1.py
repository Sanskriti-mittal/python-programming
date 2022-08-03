S=input()
new_string=""
for char in S:
    if char.isupper() or char.islower():
        unicode_of_char=ord(char)
        unicode_of_char += 1
        new_char=chr(unicode_of_char)
    else:
        new_char=char
    new_string= new_string+new_char
print(new_string)