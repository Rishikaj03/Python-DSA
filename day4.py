# name='aaabbbeeeffgg'
# newname ={}
# for i in range(len(name)):
#     key = name[i]
#     count = 0
#     for j in range (len(name)):
#         if key == name[j]:
#             count += 1
#     newname[key]=count
# print(newname)
# for i, j in newname.items():
#     print(i,j,sep='', end='')

##==========================================================================
# salary = int(input('Enter your salary'))
# rating = int(input('Enter your performance appraisal rating:'))
# increment = 0
# if rating >=1 and rating <=3:
#     increment = salary*10/100
# elif rating>=3.1 and rating <=4:
#     increment = salary*30/100
# elif rating>=4.1 and rating <=5:
#     increment = salary*40/100
# else:
#     print('Incremented Salary: ',increment + salary)

#--------------------------------------------------------------------------------------------------------------

# basic_salary = 20000

# hra_percent = 40
# da_percent = 30
# ta_percent = 10
# hra = (basic_salary * hra_percent) / 100
# da = (basic_salary * da_percent) / 100
# ta = (basic_salary * ta_percent) / 100
# gross_salary = basic_salary + hra + da + ta
# print("Basic Salary =", basic_salary)
# print("HRA =", hra)
# print("DA =", da)
# print("TA =", ta)
# print("Gross Salary =", gross_salary)

#----------------------------------------------------------------------------------------------------
#BINARY SEARCH

# def binarySearch(array, target):
#     low = 0
#     high = len(array) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if array[mid] == target:
#             return mid

#         elif array[mid] < target:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1   # outside the loop


# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]

# target = 72

# result = binarySearch(array, target)

# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at", result)
#--------------------------------------------------------------------------------------------------
#BUBBLE SORT

# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#             print(array)
#         print()

# array = [64,34,25,12,22,11,90]
# bubbleSort(array)

#=======================================================================
#ALGORITHM TO FIND THE SECURITY KEY
#INPUT: 578378923   OUTPUT: 3

# mylist = [578378923]
# newlist=[]
# for i in range(len(mylist)):
#     count=0
#     key = mylist[i]
#     j = i+1
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j +1
# print(len(newlist))
#----------------------------------------------------------------------------
#STACK IMPLEMENTATION WITHOUT SIZE LIMIT
#STACK IMPLEMENTATION WITH SIZE LIMIT
#THERE ARE TWO WAYS:- 1. LIST/ARRAY 2. LINKED LIST

#CLASS AND OBJECTS
# class Name:
#     age = 22
#     def display(self):  #Method: self is similar as 'this' of java
#         print("Hello world")
# obj = Name()
# print(obj.age)
# obj.display()

#-------------------------------------------------------------------------------
# class Student:
#     def __init__(self):
#         self.name = "Rishika"
#         self.age = 22
    
#     def display(self):
#         print("Name=", self.name)
#         print("Age=", self.age)
# stuObj = Student()
# print(stuObj)
# #---------------------------------------------------------------
# class Message:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("Class program")
# obj = Message()
# obj.shows()
# obj2 = Message()

#---------------------------------------------------------------------
#parmeterized  constructor 

# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no
    
#     def displayStudentInfo(self):
#         print("Name=", self.Name)
#         print("Age=", self.Age)
# studentObj = StudentInfo("Prakash",34,101)
# studentObj.displayStudentInfo()

#---------------------------------------------------------------------------------------
#STACK IMPLEMENTATION WITHOUT SIZE LIMIT
#push,pop,peek,isEmpty,isFull,Delete,display

# import sys
# class Stack:
#     def __init__(self):
#         self.myStack = []   #creating stack
    
#     def push(self, value):
#         self.myStack.append(value)
#         print("Element Push")
    
#     def display(self):
#         print(self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack[-1])  #start from negative 

#     def deleteStack(self):
#         self.myStack = None  #memory will be deleted.


# obj = Stack()
# print("Stack has created: ")
# while True:
#     print("1. Push operation: ")
#     print("2. Display Stack")
#     print("3. Pop operation: ")
#     print("4. Peek operation: ")
#     print("5. Delete Stack")

#     print("7. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice ==1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteStack()
#     else:
        #sys.exit()

#--------------------------------------------------------------------------------
# import sys

# class Stack:
#     def __init__(self):
#         self.myStack = []   # creating stack

#     def push(self, value):
#         if self.myStack is None:
#             print("Stack deleted")
#         else:
#             self.myStack.append(value)
#             print("Element Pushed")

#     def display(self):
#         if self.myStack is None:
#             print("Stack deleted")
#         else:
#             print(self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False

#     def pop(self):
#         if self.myStack is None:
#             print("Stack deleted")
#         elif self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Popped element:", self.myStack.pop())

#     def peek(self):
#         if self.myStack is None:
#             print("Stack deleted")
#         elif self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element:", self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = None
#         print("Stack deleted successfully")


# obj = Stack()

# print("Stack has been created")

# while True:
#     print("\n1. Push operation")
#     print("2. Display Stack")
#     print("3. Pop operation")
#     print("4. Peek operation")
#     print("5. Delete Stack")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.pop()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deleteStack()

#     elif choice == 6:
#         print("Exiting program...")
#         sys.exit()

#     else:
#         print("Invalid choice")
#------------------------------------------------------------------------------
#INPUT : 572378233 3   OUTPUT : 3

mylist = [5,7,2,3,7,8,2,3,3]
newdict = {}
for i in range(len(mylist)):
    count = 0
    key = mylist[i]
    j = 1
    while j< len(mylist):
        if key == mylist[j]:
            count+=1
        j = j+1
    if count>1:
        newdict[key]= count
max = newdict
print(max)