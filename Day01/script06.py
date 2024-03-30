# Check if a string is a palindrome or not

def is_palindrome(string):

    if string[::-1] == string:
        print(f"{string} is a palindrome  ")
    else:
        print(f"{string} is not a palindrome  ")

string1 = "radar" 
string2="string" 

is_palindrome(string1)

# Output
# radar is a palindrome

is_palindrome(string2)

# Output
# string is a palindrome