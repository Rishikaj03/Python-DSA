#WAP TO HELP APPAREL FIND THE NO OF PLOTS THAT IT CAN SELECT FOR ITS OUTLET.
#INPUT: 8  79 77 54 81 48 34 25 16       OUTPUT: 3
#THE AREAS THAT ARE IN SQUARE FORM ARE 81, 25 AND 16 SO THE OUTPUT IS 3.

# list = [79, 77, 54, 81, 48, 34, 25, 16]

#-------------------------------------------------------------------------------------------------
#function:
# def func(value, values):   #[44, 2, 3]
#     var = 1
#     values[0] = 44

# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])
#====================================================================
#APPEND
# def f(i, values = []):  
#     values.append(i)
#     print(values)  #return values
# f(1)  #calling function
# f(2)
# f(3)

#======================================================================

# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index] +=1
#     else:
#         fruit[index] = 1
#     print(fruit)
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))
#============================================================================
# #WAP to accept student name and marks from the keyboard and creates a dictionary. Also display student marks by taking student name

# n = int(input("Enter the no. of students: "))
# d={}
# for i in range(n):
#     name = input("Enter Student Name: ")
#     marks = input("Enter Student Marks: ")
#     d[name] = marks   #add key:value
# while True:
#     name = input("Enter Student Name to get Marks: ")
#     marks = d.get(name, -1)
#     if marks == -1:
#         print("Student Not Found")
#     else:
#         print("The Marks of", name, "are", marks)
#     option = input("Do you want to find another student marks[Yes|No]")
#     if option == "No":
#         break
# print("Thanks for using our application")
#=======================================================================================================
#WAP to access each character of string in forward and backward direction by using while loop
# i/p ="Learning python is very easy"

# s = "Learning python is very easy"
# n = len(s)
# i = 0
# print("Forward direction")
# while i<n:
#     print(s[i], end=' ')
#     i += 1
# print("Backward direction")
# i = -1
# while i>=-n:
#     print(s[i], end = ' ')
#==========================================================================================================
#INPUT:  abcdfjgerj abcdfijger    OuTPUT:  j
##WAP to help amold find the chracter that was missing at the recieving end but present at the sending end.
# stringSent = "abcdfjgerj"
# stringRec = "abcdfijger"
# for i in range()

#===========================================================================================================

# v=['a','e','i','o','u']
# w = input("Enter the word where we will search the vowels: ")
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels = ',found)
# print('unique vowels', len(found), 'from the given word=',w)

#=============================================================================================================
#INPUT: 6 30 50       29 38 12 48 39 55
#OUTPUT: 38 48 39

# x,y,z = map(int, input().split())
# mylist =[]
# for i in range(x):
#     a = int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>= y and j<=z:
#         print(j, end=' ')

#=============================================================================================================
# import datetime
# #date time formatting
# date = datetime.datetime.now()
# print("It's now: {:%d/%m/%Y %H:%M:%S}".format(date))
#=============================================================================================================

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)
#=============================================================================================================
# val=[2**i for i in range(1,6)]
# print(val)
#=============================================================================================================
# s=[i*i for i in range(1,11)]
# print(s)
#=============================================================================================================
#Dictionary Comprehension:
# squares = {x:x*x for x in range(1,6)}
# print(squares)

#doubles={x:2*x for x in rnge(1,6)}
#print(doubles)
#==========================================================================================================

#How to read multiple values from the keyboard in a single line:
# a,b = [int(x) for x in input("Enter 2 numbers: ").split()]
# print("Product is :",a *b)

# a,b,c = [float(x) for x in input("Enter 3 float numbers: ").split()]
# print("The Sum is: ", a+b+c)
#---------------------------------------------------------------------------------------------------------------
#using else block
# mycart = [10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everything")
#-===========================================================================================================

# while True:
#     username = input("Enter username: ")
#     password = input("Password: ")
#     if username == 'admin' and password == 'admin':
#         print("Login Succesfully")
#         break
#     else:
#         print("INVALID! Re-Enter...")

#==============================================================================================================
#TOWER OF HANOI

import time
class Tower:
    def __init__(self): 
        print("WELCOM TO TOWER OF HANOI GAME")
        print()
        print("GIven problem  A=[3,2,1]  B=[]    C[]")
        print()
        print("Expected Output A =[]  B=[]  C[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]
    
    def tower(self, item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
    
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass one Completed=============================\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass 2 Completed=============================\n")
    
    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass 3 Completed=============================\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass 4 Completed=============================\n")
    
    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass 5 Completed=============================\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass 6 Completed=============================\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B ," ","C=",self.C)
        print("Pass 7 Completed=============================\n")

obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()