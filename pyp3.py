#To take input and make list
print("Enter your favourite movies: ")
a = input("1: ", )
b = input("2:", )
c = input("3:", )
list1 = [a,b]
list1.append(c)
print(list1)
#To check if a list contains palindrome of elements.
ages=[34,31,31,34]
ages1=ages.copy()
ages1.reverse()
if(ages1==ages):
    print("It is a palindrome.")
else:
    print("It is not a palindrome")

#To count numberr of students with grade A in following tuple.
list2 = ["c","a","b","a"]
print(list2.count("a"))
list2.sort()
print(list2)




