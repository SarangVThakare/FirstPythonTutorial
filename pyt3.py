#List: It is a data-type that stores set of data values
#In python it is not at all mandatory that we should store only same type of values in a list.
marks = [93, 33, 34, 43, 98]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))

student=["Sarang",95.6,"Amravati"]
#strings: immutable(that can't be changed), mutable:(that can be changed))
student[1] = 98.2
print(student)

#Remember we can't change value of str, can't replace it using its index.
#List Slicing, all rules are according to string slicing,refer pyt2 Starting index is included, ending index is not included.
list2 = marks[2:len(marks)]
print(list2)
print(marks[-3:len(marks)])
print(marks[-3:-1])

#List Methods.
aut=["bill", "mark", "twain", "lenin"]
no=[1,2,3,3,7,4,5]
#Append Method adds one element to the last of the list.
no.append(6)
print(no)
#Sort arranges elements in list in ascending order.
no.sort()
print(no) #there's nothing like print(no.sort) => output is None
#Reverse arranges the elements in list in descending order.
no.sort(reverse=True)
print(no)
no.sort(reverse=False)
print(no)
#you may also use sort for arranging str in dictionary order.
print(aut.sort())
print(aut)
#reverse is used to reverse list without arranging in ascending or descending manner"
no.reverse()
print(no)
#insert is used to add an element at a specific site.(idx,value)
no.insert(6,300)
print(no)
#remove is used to remove an element where it occurs first.
no.remove(3)
print(no)
#pop is used to remove an element at a particular index pop(idx)
no.pop(1)
print(no)

#Tuples: Built-in data type that lets us create immutable sequence of values.
tup = (1,2,2,34,654,8,89,9)
print(tup[0])
tu = ()
print(tu)
print(type(tu))
ru = (1,)
print(type(ru))
print(ru)
ru1 = (1)
print(type(ru1))
print(ru1)
#while we make singleton tuple we must give, if we doesn't give commas then python considers it as it is integer written in parentheses.
#but when we write multiple set giving comma in last is not mandatory.
#Tuple Slicing 
print(no[-3:-1])
# Tuple Methods
#Index, tells us at what index an element occurs first.
print(tup.index(2))
#Count measures times an element occurs in a particular tuple.
print(tup.count(2))






