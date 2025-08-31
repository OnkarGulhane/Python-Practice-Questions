def sod(n):
    if n==0:
        sum=0
    else:
        d=n%10
        sum = d+sod(n//10)
    return sum


n = int(input('Enter a number:'))
ans = sod(n)
print("Sum of Digits:",ans)