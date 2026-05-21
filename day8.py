#Remove Leading  Zeros from a list of Integers
#use list slicing or a loop to remove zeros from a list of integers
#Input : [0,0,1,2,0,3,0,0,4]  Output: [1,2,0,3,0,0,4]
# Remove Leading Zeros from a List

# array = [0, 0, 1, 2, 0, 3, 0, 0, 4]

# i = 0
# while i < len(array) and array[i] == 0:
#     i += 1

# # Remove leading zeros using slicing
# result = array[i:]

# print(result)



#===========================================================================================
#Wap- create function to find first missing positive integer in a list of unsorted 
#use a loop and reposition elements to place each positive integers. INPUT: [3,4,-1,1]   OUTPUT: 2

# def firstMissingPositive(nums):

#     n = len(nums)

#     for i in range(n):

#         while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:

#             correct_index = nums[i] - 1

#             nums[i], nums[correct_index] = nums[correct_index], nums[i]

#     for i in range(n):

#         if nums[i] != i + 1:
#             return i + 1

#     return n + 1

# nums = [3, 4, -1, 1]

# print(firstMissingPositive(nums))

#==============================================================================================
#BINARY SEARCH TREE
# class BSTNode:

#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

#     # Insert Node
#     def insertNode(rootNode, nodeValue):

#         if rootNode.data is None:
#             rootNode.data = nodeValue

#         elif nodeValue <= rootNode.data:

#             if rootNode.leftChild is None:
#                 rootNode.leftChild = BSTNode(nodeValue)

#             else:
#                 BSTNode.insertNode(rootNode.leftChild, nodeValue)

#         else:

#             if rootNode.rightChild is None:
#                 rootNode.rightChild = BSTNode(nodeValue)

#             else:
#                 BSTNode.insertNode(rootNode.rightChild, nodeValue)

#     # Preorder Traversal
#     def preOrderTraversal(rootNode):

#         if rootNode is None:
#             return
#         print(rootNode.data)
#         BSTNode.preOrderTraversal(rootNode.leftChild)
#         BSTNode.preOrderTraversal(rootNode.rightChild)
        
#     #inorder traversal
#     def inOrderTraversal(rootNode):

#         if rootNode is None:
#             return
#         BSTNode.inOrderTraversal(rootNode.leftChild)
#         print(rootNode.data)
#         BSTNode.inOrderTraversal(rootNode.rightChild)

#     #postorder traversal
#     def postOrderTraversal(rootNode):

#         if rootNode is None:
#             return
#         BSTNode.postOrderTraversal(rootNode.leftChild)
#         BSTNode.postOrderTraversal(rootNode.rightChild)
#         print(rootNode.data)

#     def searchNode(rootNode, nodeValue):
#         if rootNode.data == nodeValue:
#             print("The value is found")
#         elif nodeValue < rootNode.data:
#             if rootNode.leftChild.data == nodeValue:
#                 print("The value is found")
#             else:
#                 searchNode(rootNode.leftChild,nodeValue)
#         else:
#             if rootNode.rightChild.data == nodeValue:
#                 print("The value is found")
#             else:
#                 BSTNode.searchNode(rootNode.rightChild, nodeValue)
                

# # Create BST
# newBST = BSTNode(None)

# # Insert Nodes
# BSTNode.insertNode(newBST, 70)
# BSTNode.insertNode(newBST, 50)
# BSTNode.insertNode(newBST, 90)
# BSTNode.insertNode(newBST, 30)
# BSTNode.insertNode(newBST, 60)
# BSTNode.insertNode(newBST, 80)
# BSTNode.insertNode(newBST, 100)
# BSTNode.insertNode(newBST, 20)
# BSTNode.insertNode(newBST, 40)
# BSTNode.insertNode(newBST, 10)
# # Traverse Tree
# print("Pre-order Traversal:")
# BSTNode.preOrderTraversal(newBST)
# print()
# print("In-order Traversal:")
# BSTNode.inOrderTraversal(newBST)
# print()
# print("Post-order Traversal:")
# BSTNode.postOrderTraversal(newBST)

#===============================================================================================
#we can take multiple access in single acccess box
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# finally:
#     print("Code is running")

#=================================================================================================
# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enter second integer no"))
#     print(a/b)
# except (ZeroDivisionError,ValueError) as message:
#      print(message)
#      logging.exception(message)
# print("Logging level is set up. Check 'newfile.txt for log details.")

#================================================================================================
# import csv
# f = open("employee.csv",'a')
# a=csv.writer(f)
# # a.writerow(["empID","empname","emp age"])
# empid = int(input("enter employee empid:"))
# empname = input("enter employee name:")
# age = int(input("enter employee age:"))
# a.writerow([empid,empname,age])
# print("file has created")
#=================================================================================================
# import csv
# f = open("student.csv", 'a', newline='')
# a = csv.writer(f)
# a.writerow(["Student ID","Student Name","Physics","Chemistry","Maths", "Total","Percentage","Result"])
# studId = int(input("Enter Student ID: "))
# studName = input("Enter Student Name: ")
# phy = int(input("Enter Physics Marks: "))
# chem = int(input("Enter Chemistry Marks: "))
# math = int(input("Enter Maths Marks: "))
# total = phy + chem + math
# percentage = (total / 300) * 100

# if percentage >= 40:
#     result = "Pass"
# else:
#     result = "Fail"
# a.writerow([studId, studName, phy, chem, math, total, percentage,result])
# print("File has created successfully")
# f.close()