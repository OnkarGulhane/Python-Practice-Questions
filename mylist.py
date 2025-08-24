#a = []    #creation of list 
#print(len(a))



#mylist = [11,22,'x','hello',3.9,True]
#print(len(mylist))
#print(type(mylist))


#creating list 2nd style

#mylist1 = list(mylist)
#print(mylist1)

# mylist = []
# for i in range(6):
#     n = input('Enter a no:')
#     mylist.append(n)
# print(mylist)   


#create list(array) of numbers  read from user
# mylist = []
# n = int(input('Enter how many numbers:'))
# for i in range(n):
#     no = input('Enter a number:')
#     mylist.append(no)
# print(mylist)    


# LIST COMPREHENSION

# Syntax : list = [item in sequence]
            # list = [item in sequence if condition]
# a = [n for n in range(20) if n%2!=0]
# print(a)

# mylist=[1,22,3.4,'hello',True]
# print(mylist)



# print list using advanced for loop
# for  x in mylist:
#     print(x)


# print list using while loop
# i = 0
# while i<len(mylist):
#     print(mylist[i])
#     i+=1
# # print list using forloop with index
# for i in range(len(mylist)):
# print(mylist[i])



# IMPORTANT CONCEPT FOR PYTHON >>>>REMEMBER AND PRACTICE IT UNTILL MASTERY

# i = 0
# print('[',end=' ')
# while i<len(mylist)-1:
#     if type(mylist[i])is str:
#         print('\'',mylist[i],'\'',sep='',end=', ')
#     else:
#         print(mylist[i],end=', ')
#     i+=1
# print(mylist[i],']',sep='')        


# i = 0
# print('[',end=', ')
# while i<len(mylist)-1:
#     if type(mylist[i])is str:
#         print('\'',mylist[i],'\'',sep='',end=', ')
#     else:
#         print(mylist[i],end=', ')
#     i+=1        
# print(mylist[i],']',sep='')






#### LIST SLICING ####
mylist=[1,22,3.4,'hello',True,44,78,99]
print(mylist)

# print('1st Element in list:',mylist[0])
# print('2nd Element in list:',mylist[1])
# print('3rd Element in list:',mylist[2])
# print('$4th Element in list:',mylist[3])
# print('5th Element in list:',mylist[4])
# print('6th Element in list:',mylist[5])
# print('7th Element in list:',mylist[6])
# print('8th Element in list:',mylist[7])
# print('LAST ELEMENT IN LIST:',mylist[-1])
# print('Second last Element in list',mylist[-2])


print(mylist[2:5])
print(mylist[3:])
print(mylist[:5])

print(mylist[-4:-2])

