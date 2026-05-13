# #simple if
# a=int(input("Enter any single digit: "))
# if a> 0:
#     print("positive number")
# if a<0:
#     print("Negative number")
# if a==0:
#     print("Neutral")
#--------------------------------------------------------------------------------------------

# #simple if and else
# day = input("Enter day name:  ")
# if day == "SATURDAY" or day == "saturday" or day=="Sunday":
#     print("weekend")
# else: 
#     print("working day")
#--------------------------------------------------------------------------------------------

#elseif
# per =40
# if per>=65:
#     print("Grade A")
# elif per <=65 and per>=50:
#     print("Grade B")
# else:
# #     print("Fail")

# chr=ord(input("Enter any one character: "))
# if chr >= 65 and chr <=90:
#     print("upper case")
# elif chr>=97 and chr <=122:
#     print("lower case")
# elif chr>=48 and chr<=7:
#     print("digit")
# else:
#     print("special symbol")

# #for loop - when condition or range is known.
# for i in range (5):
#     print(i)
# for i in range(2,11,2):
#     print(i)
# for i in range(5,0,-1):
#     print(i)
# for i in range (1,11):
#     print(i*2)

# for i in range (1,11):
#     for j in range (2,11):
#         print(j*i, end="\t")
#     print()
# print("      ")
# for i in range (1,11):
#     for j in range (12,21):
#         print(j*i, end="\t")
#     print()

# a=int(input("Enter marks for a: "))
# b=int(input("Enter marks for b: "))
# c=int(input("Enter marks for c: "))
# total=a+b+c
# percentage=total/3.0
# print("Total= ",total)
# print("Percentage= ",percentage)
# if a>=40 and b>=40 and c>=40:
#     print("Pass")
# else:
#     print("Fail")
# gender=input("Enter your gender M/F: ")
# if percentage>=65 and gender=="M":
#     print("Eligible for Placement")
# else:
#     print("Not Eligible")


#zip() we can take multiple range function inside zip
for i,j in zip(range(1,6),range(5,0,-1)):
    if i ==3 and j ==3:
        continue
    print(i," ", j)