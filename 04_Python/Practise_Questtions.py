#WAP to stor word menings of table and cat in a dictionary
word_meanings= {
"cat" : "a small animal" ,

"table" : [ "a piece of furniture" , "list of facts and figures"] }
print(word_meanings)

#wap to sort students learnmiong different languages in different classes from the following
#python , java , c++ , python , javascript,java python , java ,c++ ,c

subjects = { "java","C++","python","java","java","java","C++","C"
}
print(len(subjects))

#WAP to enter the marks of 3 subjects from the user and add them to a dictionary
marks = {}
physics = int(input("enter y0ur physics marks"))
chemistry = int(input("enter your chemistry marks"))
math = int(input("enter your chemistry math"))

marks.update({"physics" : physics } )
marks.update({"math" : math} )
marks.update({"chemistry" : chemistry } )

print(marks)