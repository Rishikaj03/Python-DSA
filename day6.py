#reverse each word in a string. WAP to reverse each word in a string.
#Input: "Hello world"  #Output: olleH dlrow

# string = "Hello world"
# words = string.split()   # Split string into words
# reversed_words = []
# for word in words:
#     reversed_words.append(word[::-1])   # Reverse each word
# result = " ".join(reversed_words)   # Join words back into string
# print(result)
#======================================================================================================
#Check for parenthesis. WAP to check if a string containing parenthesis is valid. InPUT:   OUTPUT: 

# WAP to check if parenthesis is valid

# string = "({[]})"
# stack = []
# valid = True
# for ch in string: 
#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if not stack:
#             valid = False
#             break
#         top = stack.pop()
#         if (ch == ")" and top != "(") or \
#            (ch == "}" and top != "{") or \
#            (ch == "]" and top != "["):
#             valid = False
#             break
# # If stack is not empty, parenthesis are not balanced
# if stack:
#     valid = False
# if valid:
#     print("Valid Parenthesis")
# else:
#     print("Invalid Parenthesis")
#===============================================================================================================
#Insertion Sort
#Real-life software examples:
# Sorting contacts alphabetically in a phonebook 📱
# Arranging songs in a playlist 🎵
# Maintaining leaderboard rankings in small games 🎮
# Sorting transaction history by date 💳
# Auto-arranging student marks in small classroom systems 🏫
# # Insertion Sort

# array = [3, 5, 8, 6, 2]
# for i in range(1, len(array)):
#     key = array[i]
#     j = i - 1

#     while j >= 0 and array[j] > key:
#         array[j + 1] = array[j]
#         j = j - 1

#     array[j + 1] = key
# print("Sorted Array:", array)

#==================================================================================================
#SELECTION SORT!

# array = [20, 12, 10, 15, 2]

# for i in range(len(array)): 
#     min = i
#     j = i + 1
#     while j < len(array):
#         if array[j] < array[min]:
#             min = j
#         j = j + 1
#     array[i], array[min] = array[min], array[i]
# print("Sorted Array:", array)

#===================================================================================================
# FIND ALL DUPLICATES IN A LIST:
# INPUT : [4,3,2,7,8,2,1,5,5]   OUTPUT: [2,5]
# WAP TO FIND ALL ELEMENETS THAT APPEAR ONE,MORE THEN ONCE IN A LIST:

# list = [4,3,2,7,8,2,1,5,5]
# newlist= []

# for i in range(len(list)):

#     for j in range(i + 1, len(list)):

#         if list[i] == list[j] and list[i] not in newlist:
#             newlist.append(list[i])

# print("Duplicate Elements:", newlist)
#=====================================================================================================
#Sort Dictionary by key or value:
#input:{"C":3,"B":2,"A":1}

# data = {"C": 3, "B": 2, "A": 1}

# # Sort by Key (Ascending)
# asc_key = dict(sorted(data.items()))

# # Sort by Key (Descending)
# des_key = dict(sorted(data.items(), reverse=True))

# # Sort by Value (Ascending)
# asc_value = dict(sorted(data.items(), key=lambda x: x[1]))

# # Sort by Value (Descending)
# des_value = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

# print("Ascending by Key :", asc_key)
# print("Descending by Key :", des_key)

# print("Ascending by Value :", asc_value)
# print("Descending by Value :", des_value)
#+=====================================================================================================
#instance is depend on the object
#TYPES OF VARIABLE(INSTANCE VAR) 
# class New:
#     def __init__(self):
#         self.a = 10 
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# # Obj1.a = 20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
#=========================================================================================================
#static variable

# class New:
#     a =10
#     def __init__(self):
#         self.name="Rishika"
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# New.a = 50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# print(Obj1.name)
#=======================================================
#for every object a  separate copy of instance variable created but in case of static variable only one copy will be created.
#variable only one copy will be created and it is accessible 
# class College:
#     collegename = "Modern College"
#     def __init__(self):
#         self.studentname = "prashant"

# principal = College()
# teacher = College()
# accountant = College()
# print("principal = ", principal.collegename,"....",principal.studentname)
# print("teacher= ", teacher.collegename,"....",teacher.studentname)
# print("accountant = ", accountant.collegename,"....",accountant.studentname)
# College.collegename="HBD"
# principal.studentname = "prashant jha"
# print("principal = ", principal.collegename,"....",principal.studentname)
# print("teacher= ", teacher.collegename,"....",teacher.studentname)
# print("accountant = ", accountant.collegename,"....",accountant.studentname)
#===========================================================================================
#LINKED LIST
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# LinkedList = LinkedList()
# LinkedList.head = Node(5)
# second = Node(10)
# third = Node(15) 
# fourth = Node(20)  

# #connecting nodes
# LinkedList.head.next = second
# second.next = third
# third.next = fourth
# # Traversing the linked list
# current = LinkedList.head
# while current is not None:
#     print(current.data)
#     current = current.next
#==================================================================================================
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None


# linkedlist = Linkedlist()

# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #connecting nodes
# linkedlist.head.next = second
# second.next = third
# third.next  = fourth

# #display linkedlist
# while linkedlist.head.next != None:
#     print(linkedlist.head.data,"|",linkedlist.head.next,"->",end=" ")
#     linkedlist.head.next = linkedlist.head.next
#==================================================================================================
# #Variable	Meaning
# self	current object
# self.head	first node
# self.tail	last node
# self.node	newly created node
# self.next	address of next node
import sys
class Node:
    def __init__(self, data):
        self.data = data #instance variable
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self,value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node  
            self.tail = self.node       #shifting pointer

    def addNodeBeginning(self,value):
        print("Add node beginning")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node

    def addNodeBetween(self, index, value):
        print("Add Node in between")
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
    

    def displayNode(self):
        while self.head is not None:
            print(self.head.data,'|', '->', end='')
            self.head = self.head.next

if __name__ == '__main__':
    object = LinkedList()
    while True:
        print('1. Add Node LinkedList : ')
        print('2. Add Node in Begginning : ')
        print('3. Add Node in Between : ')
        print('4. Add Node in End : ')
        print('5. Display Linked List : ')
        print('6. Exit : ')
        ch = int(input('Enter your choice:'))
        if ch ==1:
            value = int(input('Enter value for node: '))
            object.addNode(value)
            print('None added successfully in single Linkedlist: ')
        elif ch == 2:
            value = int(input('enter value for Node: '))
            object.addNodeBeginning(value)
        elif ch == 3:
            value = int(input('enter value for Node to add in between: '))
            index = int(input('Enter the index of the node for adding after the node '))
            object.addNodeBetween(index,value)
        elif ch == 5:
            object.displayNode()
    
        elif ch == 6:
            sys.exit()
        