# # #LINEAR SEARCH 

# # def linearSearch(array, target):
# #     for i in range(0, len(array)):
# #         if array[i] == target:
# #             return i
# #         return -1   #if target not found
    
# # array = [1,2,3,4,8,7,9]
# # target = 7
# # result = linearSearch(array, target)
# # if result == -1:
# #     print("Target value not found")
# # else:
# #     print("Element found at index", result)
    
# #     #__________________________________________________----

# # def linearSearch(array, target):
# #     for i in range(0, len(array)):
# #         if array[i] == target:
# #             return i
# #     return -1   # if target not found

# # array = [1,2,3,4,8,7,9]
# # target = 7

# # result = linearSearch(array, target)

# # if result == -1:
# #     print("Target value not found")
# # else:
# #     print("Element found at index", result)

# #----------------------------------------------------------------------------------------------------------------------------
# # 1. rstrip() To remove space at RHS
# # 2. lstrip() To remoove space at LHS
# # 3. strip() To remove space both sides

# city=input("Enter your city Name: ")
# scity=city.strip()
# if scity == 'Hyderabad':
#     print("Hello Hyderabadi.. Adab")
# elif scity == 'Chennai':
#     print("Hello Madrasi.. Vanakkam")
# elif scity == "Bangalore":
#     print("Hello Kannadiga.. Shubhodaya")
# else:
#     print("your entered city is invalid")

#_________________________________________________________________________________________________
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


#-------------------------------------------------------------------------------------------------------