
# Example 1

# myfile = open("demo.txt","r")
# data = myfile.read()
# print(data)
# myfile.close()

# Example 2

# myfile = open("demo.txt","r")
# data = myfile.read(10)
# print(data)
# myfile.close()

#Example 3 using readlines

# myfile = open("demo.txt","r")
# alllines = myfile.readlines()
# for l in alllines:
#     print(l)
# print(alllines)    



# Example 4 using with clause

# with open("demo.txt")as myfile:
#     data = myfile.read()
#     print(data)


# Copy content of 1 file into another file

myfile1 = open("demo.txt","r")
myfile2 = open("demo1.txt","w")

data = myfile1.read(12)
myfile2.write(data)

myfile1.close()
myfile2.close()