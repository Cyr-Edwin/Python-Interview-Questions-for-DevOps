# Copy contents of files named like “file1.txt …” in Folder1 to Folder2
import os
import re # regular expression
import shutil 

# Folder2 path
folder2 = "/home/edmundo/interview_questions/Day01/Folder2"

# files pathern matching

# ^ asserts the start of a line or string.It ensures that the pattern matches only from the beginning of the string.

# File  regex will match any string that starts exactly with "File".

# [0-9] is a character class that matches any single digit from 0 to 9. 

# This part of the expression allows for any single digit to appear right after "File"
# \.txt is a sequence that matches the literal string ".txt"

# $ asserts the end of a line or string. 
# This makes sure that the string ends exactly with ".txt" 

file = re.compile(r"^File[0-9]\.txt$")

try:
    # Check if Folder2 exists
    os.makedirs(folder2 , exist_ok=True)
    print(f"folder2 exist....")

except FileExistsError as e:
    print(f"{e.args[1]}/n path: {os.path.normpath(folder2)}")
          




