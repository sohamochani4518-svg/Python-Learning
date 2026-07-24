#WAP to ask user to enter the names of their 3 favourite movies and store them in a list
# movies=[]
# m1 =input("Enter the name of the movie that you like the most : ")
# movies.append( m1 )
# m1=input("Enter the name of the second best movie according to you : ")
# movies.append( m1 )
# m1=input("Enter the name of the 3rd best movie that you like : ")
# movies.append( m1 )

# print(movies)

list1 = [1,2,3,2,1]
list_copy = list1.copy()
list_copy.reverse()
if(list_copy == list1):
    print("The given list is a pallindrome .")
else:
    print("The given list is not a pallindrome .")

#WAP to calculate the number of students wuth A grade in the given tuple ,store these values in a list and arrange them in order
tup=("C","D","A","A","B","B","B","A")
print(tup.count( "A" ))

grade=["C","D","A","A","B","B","B","A"]
grade.sort()
print(grade)
