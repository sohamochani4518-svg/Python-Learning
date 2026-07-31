#set is a collection of unordered items and these items are unique and immutable for that set . however set is mutable but the elemnets of the set are immutable
#duplicate items are ignored during printing and length of set 
numbers ={1,2,3,3,3,4,5,6}
collection = set()#this is the syntax to write an empty set if we follow the traditional methid it will become an empty dictionary

print(type(numbers))
print(type (collection))

collection.add(7)
collection.add (9)
collection.add(4)
collection.add(("apple","orange","banana"))
print(collection)
print(len(collection))

collection.remove(4)
print(len(collection))
print(len(collection))

print(collection.pop())

collection.clear()
print(len(collection))
print(collection)
#list cannot be added since they are mutable while tupples can be added since they are immutable 







