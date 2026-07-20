#we can put two if statement within eaache other 
#for eg if age of driving is from 18 to 80 , then :
age=int(input("Enter your age : "))
if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("You are eligible to drive")
else:
    print ("Cannot drive")