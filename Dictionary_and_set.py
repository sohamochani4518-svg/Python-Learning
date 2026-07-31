sample_information= {

"name" : "soham",
"age" : 16 ,
"learning" : "coding",
"is_adult" : "false",
"favorite fruit " : "mango",
"marks": 98.4 ,
"languages" : ["Python","Java","c++"], #list can also be included in a dictionary 
"topics" : ("dictionary","sets") ,#tupple can also be included in a dictionary 
}
print(type(sample_information))
print(sample_information)

# we can also print specific values
print(sample_information["age"])
print(sample_information["name"])
print(sample_information["languages"])
print(sample_information["marks"])

#  we can also ammend specific elemnts of the dictionary and add new elements 
sample_information["name"] = "Soham"
sample_information["surname"] = "Ochani"

print(sample_information["surname"])
print(sample_information)
# NULL DICTIONARY 
null_dict = {}
print(null_dict)












