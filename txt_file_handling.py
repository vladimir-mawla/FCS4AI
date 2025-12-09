# Introduction to Data & File Handling

#File Types

# TXT => text file (they store plain text) - raw text
# CSV => Coma Separated Values (holds rows and columns) - table data
# JSON => APIS communicate using JSON - structured objects


# C:\folder\FCS4AI_FILEHANDLING\data\file.txt
# /Users/name/.../file.txt 


# pathlib - a modern way to create file paths that work everywhere

from pathlib import Path

path = Path("data/hello.txt")
# To write to a text file, use .write_text()
# use \n to jump on a new line
path.write_text("Hello FCS4AI!\nThis is a text file\n")


# Reading from TXT file

content = path.read_text()
# print(content)


# Appending to a file

# a => append
# w => write erases the file and rewrites it
# r => read

# Append
with path.open("a") as f:
    f.write("New line added.\n")

# Write
# with path.open("w") as f:
#     f.write("New line added.\n")

# Read
with path.open("r") as f:
    content = f.read()
    # print(content)

with path.open("a") as f:
    f.write("Another line added.\n")


