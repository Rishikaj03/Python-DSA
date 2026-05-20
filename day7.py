#Find the first non- repeating charachter:
#WAP to find the first non-repeating character in a string. INPUT: "leetcode" OUTPUT: l

# string = "leetcode"

# for ch in string:

#     if string.count(ch) == 1:
#         print("First non-repeating character:", ch)
#         break
#=======================================================================================================

#when the main problem can be divided into the same problem then we use recurrion
#recurrsion use stack technique

# #FACTORIAL SOLUTION
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(4))

#=========================================================================================================
#capatalize first solustion using recurssion
# def capitalizeFirst(arr):

#     result =[]
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])   #T +aco = Taco
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))     #['Car','Taco,'Banana]

#=============================================================================================================
#power
# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent -1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))
#===============================================================================================================
#product of array solution

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))

#===============================================================================================================
#reverse solution

# def reverse(string):
#     if len(string) <= 1:
#         return string
#     return string[len(string)-1] + reverse(string[:len(string)-1])
# print(reverse('python'))
# print(reverse('appmillers'))
#=================================================================================================================
#recurssiveRange solution

# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return num + recursiveRange(num -1)
# print(recursiveRange(6))

#===============================================================================================================

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])
# print(isPalindrome('awesome'))

#================================================================================================================
#someRecursive Solution

# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)
#     return True

# def isOdd(num):
#     if num%2 == 0:
#         return False
#     else:
#         return True
    
# print(someRecursive([1,2,3,4], isOdd))
# print(someRecursive([4,6,8,9], isOdd))
# print(someRecursive([4,6,8], isOdd))

#====================================================================================================
#winning sum
#Input: 7 9 - 8 -6 -7 8 10    OUTPUT: 19

# numCards = int(input())
# cards = list(map(int, input().split()))

# max_product = cards[0] * cards[1]
# winning_sum = cards[0] + cards[1]

# for i in range(numCards):
#     for j in range(i + 1, numCards):
#         product = cards[i] * cards[j]

#         if product > max_product:
#             max_product = product
#             winning_sum = cards[i] + cards[j]

# print(winning_sum)

#============================================================================================================
#TREE - is a nonlinear data structure with heirchial relationships between its elements without having any cycle.
#The file system on a compiler.

# class Tree:
#    def __init__(self,data):
#      self.data = data
#      self.child = []

#    def addChild(self, object):
#      self.child.append(object)
#      print("Tree Node Added")

#    def __str__(self, level = 0):
#      ret =" "* level + str(self.data) + "\n"
#      for ch in self.child:
#        ret += ch.__str__(level+1)
#      return ret

# rootNode = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee= Tree("Coffee")
# NonAlcoholic = Tree("NonAlcoholic")
# Alcoholic= Tree("Alcoholic")

# rootNode.addChild(Hot)  #Left
# rootNode.addChild(Cold)  #Right
# Hot.addChild(Tea)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)
# print(rootNode)

#==============================================================================================

# class Tree:
#    def __init__(self,data):
#      self.data = data
#      self.child = []

#    def addChild(self, object):
#      self.child.append(object)
#      print("Tree Node Added")

#    def __str__(self, level = 0):
#      ret =" "* level + str(self.data) + "\n"
#      for ch in self.child:
#        ret += ch.__str__(level+1)
#      return ret
   
# rootNode = Tree("N1")
# N2 = Tree("N2")
# N3 = Tree("N3")
# N4 = Tree("N4")
# N5 = Tree("N5")
# N6 = Tree("N6")
# N7 = Tree("N7")
# N8 = Tree("N8")

# rootNode.addChild(N2)  #Left
# rootNode.addChild(N3)  #Right
# N2.addChild(N4)
# N2.addChild(N5)
# N4.addChild(N7)
# N4.addChild(N8)
# N3.addChild(N6)
# print(rootNode)
#================================================================================================
#Array Rotation:
# Input: [1,2,3,4,5] rotated by 2 steps [4,5,1,2,3]   OUTPUT:[4,5,1,2,3]

array = [1, 2, 3, 4, 5]

k = 2   
result = array[-k:] + array[:-k]

print("Rotated Array:", result)