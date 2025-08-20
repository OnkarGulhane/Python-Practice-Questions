sum = 0
n = int(input('Enter a number:'))
n1=n
while n>0:
    d = n%10
    sum+=d**3
    n = n//10
print('Sum of cube of digits:',sum)    

if(n1==sum):
    print(n1,'is an armstrong number')
else:
    print(n1,'is not an armstrong number')