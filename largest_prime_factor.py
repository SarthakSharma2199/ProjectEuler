import math
num=600851475143
largest_prime_factor=1
for i in range (1, round(math.sqrt(num))):
    if(num%i==0):
        isthefactorprime=1
        for j in range(2, round(math.sqrt(i))):
            if(i%j==0 ):
                isthefactorprime=0
        if(isthefactorprime==1):
            largest_prime_factor=i
print(largest_prime_factor)

        
