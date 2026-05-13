# mylist = ["prashant","ankush","Komal","Ashish",77,"sandip",60.52,"Rishika"]
# print(mylist)
# print(type(mylist))#<List>
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])#print array 2nd to 5th
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# mylist[1]="Priya"
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print("Not available")


# mylist.append('harsh')
# mylist.append("laxman")
# print(mylist)

# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("sanket")
# print(mylist)

# newlist=mylist.copy()
# print(mylist)

# mylist = [['prashant','jha'],['85.56'],[440022,"yyy"]]
# print("example of multi dimensional list: ")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list2=[50,25.50,'prashant']
# del list2[2]
# print(list2)

# list2=[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name="prashant"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[44,22,77,0,9,88]
# mylist.sort()
# #mylist.sort(reverse=True)#for descending order
# print(mylist)

# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,77,0,9,88]
# for i in mylist:
#     print(i)

# list1=[0,1,4,0,2,5]
# for i in list1:
#     if i== 0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)

# #FIND SECOND LARGEST Element
# list1=[7,3,9,2,8]
# list1.sort()
# print(list1[-2])

#Q# 
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# #Q#
# a=[1,2,3,4,5]
# print(a[3:0:-1])

# ##Q#
# arr=[[1,2,3,4], [4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i], end = " ")

# #Q#
# fruit_list1=['Apple','Berry','Cherry','Papaya']
# fruit_list2= fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='Guava'
# fruit_list3[1]='Kiwi'

# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0]=='Guava':
#         sum+=1
#     if ls[1]=='Kiwi':
#         sum+=20
# print(sum)

# #Q#
# #Find the intersection of the three arrays: Find the common elements in three arrrays
# #Logic: Use three sets to keep track of common elements between the arrays.



#*QUESTION*
mylist=[]
N = int(input("Enter the value of N: "))
for i in range(N):
    val = int(input("Enter the value: "))
    mylist.append(val)
print(len(mylist))
sum=0
for i in range(len(mylist)-1):
    if i+1 in range(len(mylist)):
        sum += abs(mylist[i]-mylist[i+1])
print(sum)