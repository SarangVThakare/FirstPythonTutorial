#escape sequence characters.
str1 = "Sarang.\nHe is a web developer."
#every space after \n will be seen.n: next line
str1 = "Sarang.\tHe is a web developer\t\t\t."
print(str1)
str2 = "Happy" 
str3 = " Moment"
str4 = str2+str3+"       "   #This is termed as concatenation.
print(str4)
len1 = len(str4)
print(len1)
print(len(str4))
#for not confusion, we may use, double inverted commas when our string possess single apostrophe and vice versa."Sarang's"
#while couunting length it also counts spaces..
"""Indexing, it gives no to the string
and the numbering starts from 0 """

pass1 = "IISc_India$"
ch1=pass1[3]
print(ch1)
print(pass1[3])
print(pass1[-3])
"""oops, we can't manipulate our that character with indexing.
like pass1[3] = "@"
makes no sense"""
"""Slicing, it cuts required data from a string,
"""
science= "Python, Java"
print(science[2:4])
print(science[2:len(science)])

time="money"
print(time[2:])
print(time[:len(time)])
print(time[1:])
print(time[:])
f=time[1:3]
print(f)

"""if you don't write anything at start it interpretes it as 0 and if anything not written at last it interpretes it as last index of string.
in slicing it's index no so last no is not present in the slice but starting index is present.
"""
fruit="jackfruit"
print(fruit[-3:-1])
#negative indexing is an exclusive feature in python, in it indexing starts from last letter assigned -1 last second -2 and so on.
#but we can't take last letter in negative slicing, by number instead write last len() to add lst element and 
#also don't mix non-negative with negative slicing.
#String Functions
print(fruit.endswith("uit")) #checks whether the string endswith that string
print(fruit.endswith("jac"))
print(fruit.capitalize()) # it capitalizes the first character
fruit1 =fruit.capitalize()
print('\n',fruit1)
#we may directly print string with capitalizatin or may modify it in a different manner.
print(fruit.replace("t","ty")) #var.replace("old", "new")
fruit2=fruit.replace("t","ta")
print(fruit2)
#find function, it returns 1st index of 1st occurrer
fruit3=fruit.find("rui")
print(fruit3)
print(fruit.find("jac"))
print(fruit.find("x"))# here -1 index will be the output which refers that no such index is there, 
#as negative index are not practical, remember negative indexing is just for slicing.
#count function counts the occurrence of a substring.
print(fruit.count("ac"))

#Conditional Statements
"""syntax: rules or correct way to write a code
"""
age = 21
if(age>=18):
        print("He can now get a license.")
        print("Can do stock marketing.")
tl = "Green"
if(tl == "red"):
    print("Stop")
elif(tl != "Green"):
    print("Stop")
elif(tl == "Green"):
    print("Go")
#here, colon after writing statements is necessary, 
#and also if once one statement is executed, then further statement is not required.
#if statement refers to compulsion whereas elif is checked if, if statement is False.every else statement possess a if accompanied with it.
a = 40
if(a > 3):
     print("Its greater than 3")
if(a<=10):
     print("Its less than 10")
elif(a>=10):
     print("None")

b = 65
if(b<1):
     print("Y")
elif(b<9):
     print("N")
else:
     print("Nor")
#indentation means proper spacing.
#Nesting, it means we are adding conditions in if statement.
age = 99
if(age>=18):
    if(age>=90 and age<95):
          print("Advice, Don't Drive.")
    else:
        print("Can Drive")
else:
    print("Its Okay")

"""Important Concept:
if checks a statement and if its not true then only elif further checks it
else is written at last and runs only when all commands are stopped.
then when you do nesting the nested if runs only if the main 'if' gives output True
otherwise you don't have to nest.
"""