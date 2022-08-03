def get_lower_and_upper_case_letters(word):
    # Complete this function
    string_upper=""
    string_lower=""
    for char in word:
        var=char.isupper()
        if var:
            string_upper += char
        else:
            string_lower += char
    print(string_upper)
    print(string_lower)
        

word = input()
# Call the get_lower_and_upper_case_letters function
get_lower_and_upper_case_letters(word)