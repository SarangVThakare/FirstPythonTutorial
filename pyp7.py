#Create a new file and add data in it.
f = open("demo.txt", "w")
f.write("Hi everyone\nWe are learning File I/O")
f.close()

with open("demo1.txt", "w") as d:
    d.write("Hi everyone.\n We are learning File I/O")
#To replace some words in a file
with open("demo.txt") as t:
    data = t.read()
    
data2 = data.replace("are", "okay")
with open("demo.txt", "w") as m:
    m.write(data2)

#Search if any word exists in a file.
with open("demo.txt") as d:
    data3 = d.read()
if(data3.find("learning") != -1):
    print("Found")
else:
    print("Not Found")

#Check for line
def check():
    word="learning"
    d=True
    with open("demo.txt") as g:
        i=1
        while d:
            d = g.readline()
            if(word in d):
                print("found on line no: ", i)
                return
            i+=1
        return -1
check()

#From a file containing numbers separated by commas, print the count of even numbers.
with open("demo3.txt", "w") as j:
    j.write("1,2,3,4,5,6,7,8")

with open("demo3.txt", "r") as j:
    dw = j.read()
    count=0
    nums= dw.split(",")
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1

print(count)    
            

import os
os.remove("demo3.txt")
