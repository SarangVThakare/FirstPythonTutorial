#File I/O means using python to perrform operations on file(read and write data).
#Types of Files: 1. Text Files: .txt, .docx, .log, etc.
#                2. Binary Files: .mp4, .mov, .png, .jpeg,etc.
#ignore these lines and write something in demo.txt
f=open("demo.txt", "w")
f.close()
#...
#Open a File:
f = open("demo.txt", "r")
a = f.read() #outputs it in form of str
print(a)
f.close() #to close a file
"""
Character: Meaning
r:open for reading(default)
w:open for writing, truncating the file first
x: create a new file first and open it for writing
a: open for writing, appending to the end of the file if it exists.
b: binary mode
t: text mode
+ open a disk file for updating(reading and writing)

eg:"rt" means read and text mode, text mode is default for binary you have to specify b.
"a+", means we have to both append and read the file. Similarly"w+", for both writing and reading.
"""

#Reading a File:
f = open("demo.txt", "r")
data = f.read(5) #no of characters to be read
print(data)

data1 = f.readline()
print(data1)#here as newline character exists in txt file so it is read by python and a blank line is created.
data2 = f.readline()
print(data2)
#empty space after once all data is read.
#so to go back we have to close the file and then reopen it.
f.close()
f = open("demo.txt", "w")
f.write("I want to learn JS\nI also have to revise CSS")
#Write doesn't allow to write multiple characters.
f.close()
#If you open any file in w or a mode, if it doesn't exist then it would create the file.
#While, in read mode, it would show error.
f=open("demo1.txt", "w")
f.close()
#r+ mode is for writing, without truncating file. But, overwriting from start.

f=open("demo1.txt", "r+")
f.write("abc")
f.close()

f=open("demo1.txt", "a+")
f.write("abc")
f.close()
#a+ mode is for adding to last without truncating.

#with syntax
with open("demo.txt", "r") as f:
    data=f.read()
    print(data)
#don't need to close, with syntax automatically closes it.

with open("demo.txt", "w") as f:
    f.write("new data")

#Deleting a File, using the OS(operating system) Module, module(like a code library is a file written byy another programmer that generally has a functions we can use.)

import os
os.remove("demo.txt")

import os
os.remove("demo1.txt")

















