import os
import re # regular expression
import shutil 

# Folder2 path
folder2 = "/home/edmundo/interview_questions/Day01/Folder2"
try:
    # Check if Folder2 exists
    os.makedirs(folder2 , exist_ok=True)

except FileExistsError as e:
    print(f"{e.args[1]}/n path: {os.path.normpath(folder2)}")
          




