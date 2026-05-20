# mydict={
#     101:"prashant",102:"ashish","103":"mohini","104":"trivani",101:"ashish",104:"ashish"
# }
# print(mydict)

#with the help of key print value
# a=mydict[102]
# print(a)

# mydict[102]="peter"
# print(mydict)

# for x in mydict:
#     print(x)

# for x in mydict.values():
#     print(x)

# #printing key and vaalues both
# for x,y in mydict.items():
#     print(x,y)

# mydict["mobile_no"]=4658761234
# print(mydict)

# mydict.pop(101)
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr={}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# sum=0
# for k in arr:
#     sum += arr[k]
# print(sum)


# my_dict={}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)


# my_dict={}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print (dict[_])

# rec = {"Name": "Python", "Age":"20"}
# r =rec.copy()
# print(id(r))
# print(id(rec))
# print(id(r) == id(rec))

# rec = {"Name": "Python", "Age:": "20", "Addr": "NJ","Country":"USA"}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {"Name": "Python", "Age:": "20", "Addr": "NJ","Country":"USA"}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)

#---------------------------------------------------------------------------------
#9. Find the key with the Maximum value in  a dictionary
#Input- {"a":50,'"B":30, "C": 20}

# d= {"A":50,"B":30, "C": 20}
# print(max(d))
#-----------------------------------------------------------------------------


#------------------------------------------------------------------------------

# #Count frequency of Elements in a list using dictionary
# lst = [1,2,2,3,3,4,5]
# freq = {}
# for i in lst:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)
#________________________________________________________________________________________


