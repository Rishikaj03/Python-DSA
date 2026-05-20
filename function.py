# #function is a self executable block which we can run as many time we want. Function is created aoutside the class and is called by function name. method is created inside the class nd called by creating an object.

# def hello():
#     print("hello world")
# hello() #calling function.
# hello()

#----------------------------------------------------------------------------------------------------------------------------------

# def arithmatic():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# # print(arithmatic())  #it is possible to return multiple value.
# result = arithmatic()
# print("Arithmatic = ", result)

#-------------------------------------------------------------------------------------------------------------------------------------
#HOW MANY TYPES OF ARGUMENT WE PASS IN FUNCTION.
# 1. POSITIONAL ARGUMENT
# 2.KEYWORD
# 3. DEFAULT
# 4. VARIABLE LENGTH / VARIABLE NUMBER OF ARGUMENTS
#------------------------------------------------------------------------------------------------
#1. POSITIONAL ARGUMENT

# def arithmatic(a,b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# # print(arithmatic())  #it is possible to return multiple value.
# result = arithmatic(5,5) #positional argument
# print("Arithmatic = ", result)

#------------------------------------------------------------------------------------------------
#2. KEYWORD ARGUMENT

# def credential(username, password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid credentials")
# credential(username="admin", password="admin") #calling function.
# #keyword name and parameter name must be same.

#---------------------------------------------------------------------------------------------------------
#3.  DEFAULT Argument

# def cityName(city="Pune"):  #default argument
#     print(city)
# cityName("Nagpur")
# cityName("Mumbai")
# cityName() #default

#-----------------------------------------------------------------------------------------------------------
#VARIABLE LENGTH ARGUMENT / VARIABLE NUMBER OF ARGUMENT

# def cityName(*name):
#     print(name)
# cityName("Nagpur","Delhi","Mumbai","Pune")
#-------------------------------------------------------------------------------------------------------------

#MODULARITY APPROACH IN FUNCTION

# import sys
# def add():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a+b)

# def sub():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a-b)

# def div():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a/b)

# def mul():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a*b)

# while True:
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Division")
#     print("4. Multiplication")
#     print("5. Exit")
#     choice = int(input("Enter you choice: "))
#     if choice == 1:
#         add()  #calling function
#     elif choice == 2:
#         sub()  #calling function
#     elif choice == 3:
#         div()  #calling function
#     elif choice == 4:
#         mul()  #calling function
#     elif choice == 5:
#         sys.exit()

#------------------------------------------------------------------------------
# def findBiggestNumber(sampleArray):   #[5,7,9,2,3,4]
#     biggestNumber = sampleArray[0]
#     for index in range(1,len(sampleArray)):              #O(N)
#         if sampleArray[index]> biggestNumber:
#             biggestNumber = sampleArray[index]
#     print(biggestNumber)
# sampleArray=[5,7,9,2,3,4]
# findBiggestNumber(sampleArray)
#---------------------------------------------------------------------------------