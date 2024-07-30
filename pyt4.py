#Dictionaries used to store values in key:value pairs. They are unordered(don't have index for keys), mutable(like list) and don't allow duplicate keys.
d1 = {
  "name" : "Sarang",
  "age" : 17, "is_adult": False, 
  "marks" : 95.6,
  "topics": ["fire","ice",34,99.99, True ],
  12.43:23.66,
  ("tuple, list can't be key as its mutable") : 23 ,


}#here indentation in spacing of brackets is not necessary. But comma must not be forgotten after everry key-value pair.

print(d1)
print(type(d1))
print(d1["marks"])
d1["marks"] = 98.2
print(d1["marks"])
#we can add element
d1["mark10"] = 100
print(d1)
#many times null dict is created, and then elements are added in it.
null_dict = {
}
print(null_dict)
null_dict["happy"] = "moment"
print(null_dict)

#Nesting in dictionary
d2 ={ "subjects" : {
      "phy" : "mechanics",
      "chem" : "physical",
      "math" : "calculus",
                   },
  "class" : 12
    }
print(d2)
print(d2["subjects"])

#Dictionary Methods:
#.keys, returns all keys, only main keys are returned not nested keys.
print(d1.keys())
#now you may typecast it, into list for further mutation.
print(list(d1.keys()))
#prints no of keys in dictionary.
print(len(d1))
print(len(list(d1.keys())))
#print all values, len, makes it a list.
print(d1.values())
print(len(list(d1.values())))

#returns all key value pairs as tuples
print(d1.items())
#you may convert it into list of tuples and then may manipulate it.
a = list(d1.items())
print(a[3])
#returns key according to value, it is useful as if a key not in dict is put,
# it doesn't show error,but in print(d1["name2"]), error will be thrown and further code execution would terminate.
print(d1.get("name2"))
#print(d1["name2"])

#inserts specified items to dictionary
d3 = {
"life" : "Thrill"
}
d4 = {
    "humour" : "laughter"
}
d3.update(d4)
print(d3)
d3.update({"piano":"music", "fun": "24*7", "life": "stop"})#use curly braces
print(d3)
#if same value is written it overwrites it.

#Sets in Python, is the collection of unordered items(it may not print in the order we have written).
# Each element in set is immutable and unique(it would ignore the repeated values and prints one time only).
#Therefore, only boolean, tuple, str, float, int is allowed and dict and list are not allowed.

set1 = {1,2,2,"jockey",2,3,4, "str", "str"}
print(set1)

#To write null set,we can't simply give curly braces as its syntax of dict.
f1 = {}
print(type(f1))
f2 = set()  #here it's simple brackets
print(type(f2))

#Set Methods, set is mutable but it's individual elements are immutable.
#dict.add it adds elements in set.(not list, tuple allowed)
f2.add(23)
f2.add(23)
f2.add(True)
f2.add((1,2,3))
print(f2)#look it ignores repeated values.
#removes an element, if you try to remove an element which doesn't exist it will throw error.
f2.remove(23)
#f2.remove(23) will show error as now 23 doesn't exist in f2.
print(f2)
#hashing means to mutate any value. unhashable means which is immutable.
#clear method empties the set.
f2.clear()
print(len(f2))
#pop method removes a random value.
c1 = {3,4,3,3,5,35,5}
print(c1.pop())
print(c1.pop())
print(c1.pop())
print(c1.pop())
print(c1)

#Union and intersection method in python
#union combines both ignoring repetition.

set2 = {1,2,3}
set3 = {2,3,4,5}
set4 = set2.union(set3)
print(set4)
print(set2)
#doesn.t affect original set
#intersection combines common values

