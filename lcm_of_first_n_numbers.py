# Python program to find the smallest number evenly 
# divisible by all number 1 to n 
import math

# Returns the lcm of first n numbers 
def lcm(n): 
	ans = 1	
	for i in range(1, n + 1): 
		ans = (ans * i)//math.gcd(ans, i)		 
	return ans 

# main 
n = 20
print(lcm(n) )
