# #WAP to check if a number entered by a user is even or odd
# num=int(input("Enter a number : "))
# rem= int(num % 2)
# if(rem == 0):
#     print("The entered number is even .")
# else:
#     print("The number entered is odd")


# #WAP to find the greatest of 3 numbers entered by a user
# num1=float(input("Enter 1st number : "))
# num2=float(input("Enter 2nd number : "))
# num3=float(input("Enter 3rd nummber : "))

# if(num1 > num2 and num1 > num3):
#     print("Number 1 is the largest number ")
# elif(num2>num1 and num2 > num3):
#     print("Number 2 is the largest number ")
# else:
#     print("Number 3 is the largest number")

# #WWAP to check if a number is a multiple of 7 or not 
# n=float(input("Enter a number : "))
# r=n % 7
# if(r == 0):
#     print("The entered number is a multiple of 7")
# else:
#     print("The given number is not a multiole of 7")


 #WAP to find the greatest of 4 numbers entered by a user
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print("The greatest number is:", n1)
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    print("The greatest number is:", n2)
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    print("The greatest number is:", n3)
else:
    print("The greatest number is:", n4)










