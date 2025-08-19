# list of list is nothing but matrix
mylist =[ [1,2,3,4],[11,22,33,44],[77,87,99,7] ] 
print(mylist)
# #****OPTION 1 USING ADVANCED FOR LOOP****
for row in mylist:
    for col in row:
        print(col,end=' ')
    print()    


#****option 2 using for loop****

    i = 0
    while i<len(mylist):
        j=0
        while j< len(mylist[i]):
            print(mylist[i][j],end=' ')
            j+=1
        print()    
        i+=1    

        