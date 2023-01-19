import re
#your code goes here

def is_valid_phone_number(phone_number:str):
    pattern = "^[18 9]{1}[0-9]{7}$"
    if re.match(pattern, phone_number):
        return "Valid"
    else:
        return "Invalid"

phone_number:str = input()
print(is_valid_phone_number(phone_number))

"""
Phone Number Validator


You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid

You can use a regular expression to check if the input matches the given pattern.
"""