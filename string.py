# name="prashantjha"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[4])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

#_____________________________________________________________________________________________

# s="Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#____________________________________________________________________________________________

# name="prashant"
# sal=5000
# age=28
# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")
#____________________________________________________________________________________________

# name ="prashant"
# for i in name:
#     print(i)

#-----------------------------------------------------------------------------------------
#WAP to remove duplicate character
# name ="prashant"
# newname =""
# for i in name: #by default i=0
#     if i not in newname:
#         newname +=i
# print(newname)
#-----------------------------------------------------------------------------------------
# #WAP to reverse name
# name ="prashant"
# newname =""
# N = len(name)
# for i in range(N-1,-1,-1): #by default i=0
#   newname += name[i]
# print(newname)
#--------------------------------------------------------------------------------------------

# #Palindrome
# name="racecar"
# #name= "help4code"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")
#--------------------------------------------------------------------------------------------------

#Count vowels and consonants

# vowels =['a','e','i','o','u']
# name = "hello"
# cons =0
# vow=0
# for i in name:
#     if i in vowels:
#         vow +=1
#     else:
#         cons +=1
# print("consonent = ", cons)
# print("vowels = ", vow)
#-------------------------------------------------------------------------------------------------
#ANAGRAM- check if both string are same
#"listen and silent"

#-------------------------------------------------------------------------------------------------
# #Count a word in a string.
# name="Hello world"
# words =name.split()
# print("count of words:",len(words))

#--------------------------------------------------------------------------------------------

#string----> input: gasgg54@vscsd!s* OUTPUT:4

#--------------------------------------------------------------------------------------------

# #Title case
# #WAP to convert th first letter each word
# s="this is a test"
# print(s.title())

#----------------------------------------------------------------------------------------------
# print('prashantjha777'.isalnum())
# print('prashantjha777'.isalpha())
# print('777f'.isdigit())
# print('dghasfhgjhak'.islower())
# print(' '.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant'.istitle())
# print(' '.istitle())
# print(' '.isspace())
# print(' '.startswith("He"))
# print(' '.endswithwith("lo"))
#------------------------------------------------------------------------------------------------------

# print("Prashant".find("r"))
# print("Prashant".index("r"))
#---------------------------------------------------------------------------------------------------------

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#---------------------------------------------------------------------------------------------------------
# n=int(input("Enter the no. of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
#------------------------------------------------------------------------------------------------------------
# n=int(input("Enter the no. of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print()
#------------------------------------------------------------------------------------------------------------

# n=int(input("Enter the no. of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

#-------------------------------------------------------------------------------------------------------------
# import time
# n=int(input("Enter the no. of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):
#         time.sleep(3)
#         print("*",end=" ")
#     print()
#---------------------------------------------------------------------------------------------------------------
#Product of array -INPUT[1,2,3,4] Output[24,12,8,6]
#return an array where each element is the product of all elements in the array  except itself.