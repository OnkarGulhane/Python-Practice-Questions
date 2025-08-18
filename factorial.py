# n = int(input('Enter a number:'))
# ans = 1
# while n>0:
#     ans  = ans * n
#     print('Intermediate answer:',ans)
#     n = n-1
# print('Factorial of given no is:',ans)    

n = int(input('Enter a number:'))
ans   = 1
for i in range(1,n+1):
    ans  = ans * i
print('Factorila of given no is :',ans)
