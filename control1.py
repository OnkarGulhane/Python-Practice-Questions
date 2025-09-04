x = int(input('Enter a number:'))
if x%5==0:
    if x%7==0:
        print(x,'is divisible by 5 and 7 both')
    else:
        print(x,'is divisible by 5 but not divisibe by 7')
else:
    print(x,'is not divisible by 5')        
