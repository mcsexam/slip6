def print_case_alphabets(input_string):
    lowercase_alphabets = []
    uppercase_alphabets = []

    for char in input_string:
        if 'a' <= char <= 'z':
            lowercase_alphabets.append(char)
        elif 'A' <= char <= 'Z':
            uppercase_alphabets.append(char)

    print(f"Lowercase alphabets: {''.join(lowercase_alphabets)}")
    print(f"Uppercase alphabets: {''.join(uppercase_alphabets)}")


my_string = "Hello World 123 Python"
print_case_alphabets(my_string)
