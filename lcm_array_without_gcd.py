# Pyhton3 program to find LCM of array 
# without using GCD. 

# Returns LCM of arr[0..n-1] 
def LCM(arr, n): 
	
	# Find the maximum value in arr[] 
	max_num = 0; 
	for i in range(n): 
		if (max_num < arr[i]): 
			max_num = arr[i]; 

	# Initialize result 
	res = 1; 

	# Find all factors that are present 
	# in two or more array elements. 
	x = 2; # Current factor. 
	while (x <= max_num): 
		
		# To store indexes of all array 
		# elements that are divisible by x. 
		indexes = []; 
		for j in range(n): 
			if (arr[j] % x == 0): 
				indexes.append(j); 

		# If there are 2 or more array 
		# elements that are divisible by x. 
		if (len(indexes) >= 2): 
			
			# Reduce all array elements 
			# divisible by x. 
			for j in range(len(indexes)): 
				arr[indexes[j]] = int(arr[indexes[j]] / x); 

			res = res * x; 
		else: 
			x += 1; 

	# Then multiply all reduced 
	# array elements 
	for i in range(n): 
		res = res * arr[i]; 

	return res; 

# Driver code 

arr = []; 
for i in range(1, 20):
    arr.append(i)
n = len(arr); 
print(LCM(arr, n)); 

# This code is contributed by chandan_jnu 
