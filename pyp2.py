"""
#To count some substring in a particular string.
name = input("Name: ", )
print(len(name))
print(name.count("$"))

#Conditional Grading(Report Card)
marks = int(input("Enter your marks: ", ))
if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=70):
    print("Grade C")
else:
    print("Grade D")

#To check if a number is odd or even
num = int(input("Enter a number:", ))
num1 = num%2
if(num1 == 0):
    print("Yes, ", num, "is an even number.")
elif(num1 != 0):
    print("Yes, ", num, "its an odd number.")
else: 
    print("Sorry")
   
a1 = float(input("1: " ))
a2 = float(input("2: " ))
a3 = float(input("3: " ))
if (a1>a2 and a1>a3):
    print("Number 1 is largest")
elif (a2>a1 and a2>a3):
    print("Number 2 is largest")  
elif (a3>a2 and a3>a1):
    print("Number 3 is largest")
else:
    print("Two or three numbers are equal.")


if (a1>a2 and a1>a3):
    print("Number 1 is largest")
elif(a2>=a3):
    print("Number 2 is largest")
else:
    print("Number 3 is largest")
 """
no=int(input("Check if its multiple of 7: ", ))
if(no%7 == 0):
    print(no, "is a multiple of 7.")
else:
    print(no, "is not a multiiple of 7.")
    