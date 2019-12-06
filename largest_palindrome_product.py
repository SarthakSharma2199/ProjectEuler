largest_palindrome=0
for i in range(100, 999):
    for j in range(100, 999):
        num=i*j
        temp=num
        rev=0
        while temp:
            rev=rev*10+(temp%10)
            temp=temp//10
        if(rev==num and num>largest_palindrome):
            largest_palindrome=num
print(largest_palindrome)