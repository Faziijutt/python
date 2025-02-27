

# problem no 3

import pyttsx3
engine = pyttsx3.init()
engine.say("hey... my name is Faizan ... How are you Faizan")
engine.runAndWait()

# problem no 4

import os

# Specify the directory path
directory_path = '.'  # '.' represents the current directory

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)