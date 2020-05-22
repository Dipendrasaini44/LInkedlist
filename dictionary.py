thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one:

for x in thisdict:
    print(x)

# Print all values names in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# use the values method to get the dictionary values

for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() method:

for x,y in thisdict.items():
    print(x,y)


# Loop through both keys and values, by using the items() method:

for x in thisdict:
    if "model" in thisdict:
        print("yes")


# To determine how many items (key-value pairs) a dictionary has, use the len() function.

print(len(thisdict))



# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict['dipendra']='Saini'
newdict =thisdict.copy() #not gona work

print(thisdict)


# The pop() method removes the item with the specified key name
thisdict.pop("year")
print(thisdict)


# The popitem() method removes the last inserted item

thisdict.popitem()
print(thisdict)

# remove the value using the key

del thisdict['model']
print(thisdict)

thisdict['place']="ALwar"
thisdict['MOb']="8949514490"
# delete the whole dictionary

# del thisdict  ==> delete the whole dictionary

# print(thisdict)

print(thisdict)

# clear function remove the entery from the dictionary do empty but not delete

thisdict.clear()
print(thisdict)


# You cannot copy a dictionary simply by typing dict2 = dict1

# Make a copy of a dictionary with the copy() method:

thisdict = newdict.copy()
print(thisdict)


thisdict.clear()
# Another way to make a copy is to use the built-in function dict()
thisdict = dict(newdict)
print(thisdict)


# A dictionary can also contain many dictionaries, this is called nested dictionaries.

family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


# It is also possible to use the dict() constructor to make a new dictionary:

mydict = dict(name='dipendra',lastname='saini',sex="Male")
print(mydict)


## finish the dictionary 
