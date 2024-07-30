#loops
#while condition, till the condition is true the loop will iterate.
#Iteration means repetition, iterator means that count. 
count = 1
while count<5:
    print("Hello", count)
    count+=1

while count>=1:
    print("Hello", count)
    count-=1

#Don't create an infinite loop as it would crash our server or website.
#To print no from 1 to 100
i = 1
while i<=100:
    print(i)
    i+=1
#To print no from 100 to 1
while i>=2:
    i-=1
    print(i)
#To print multiplication table of 9
m=1
while m<=10:
    print(9*m)
    m+=1

j = 9
while(j<=90):
    print(j)
    j+=9

k = 1
while(k<=10):
    print(k*k)
    k+=1

t = (1,2,3,4,5,6,7,8,9)
s = 1
#To search something in tuple, eg 8
# while s<=7:
#     s+=1
# print(s)

g=0
while g<len(t):
    if(t[g]==8):
        print("8 is found a idx: ", g)
    else: 
        print("Searching.....")
    g+=1
#See, here loop also continues even if the number is found.
#Break is used to terminate a loop when encountered.

h = 0
while h<len(t):
    if(t[h]==8):
        print("Found at idx: ", h)
        break
    else:
        print("Finding..")
    h+=1
print("Loop terminated")

#Continue: terminates execution in the current iteration and continues execution of the loop.

z = 0
while z<=5:
    if(z==2):
        z+=1
        continue #skip
    print(z)
    z+=1

#here due to continue, when z was equal to 2 it skips the lower part and restarts the loop.

y = 0
while y<=10:
    if(y%2==0):
        print(y, "is even number.")
        if(y==8):
            print("Happy")
            break 
    y+=1


#For loops are used for sequential traversal, in list, str, tup,etc.
list1 = {1,2,3,4,5}

for numb in list1:
    print(numb)

name = "sarang"
for ch in name:
    if(ch=="n"):
        print("n found")
        break
    print(ch)
else: 
    print("all charaters printed")
#else it is completely optional and is used to print something after complete loop runs. 
#Neverthless, you may write it outside but it would print everytime, code is executed.
print("Okay")

t1 = (1,4,9,16,25,36,49,25)
for d in t1:
    print(d)
else:
    print("All squares are printed")
x = 25
idx1 = 0
for d in t1:
    if(d==x):
        print("25 is fought at idx: ", idx1)
    idx1+=1

#Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 by default, and 
#stops before a specified number.
#Range(start, stop(that no is not included), step(int only float not allowed)), basically we can use as data type.
print(range(5))
se1 = range(5)
print(se1[3])
for el in range(5):
    print(el)
for el in range(1,5):
    print(el)
for el in range(20,50,5):
    print(el)

#Linear search, means we are line wise checking numbers.

#Pass statement: It is a null statement that does nothing. It is used as placeholder for the future code. 
#Unlike, continue it just says that the for loop is empty, else error will be shown.

for mo in range(7):
    pass







