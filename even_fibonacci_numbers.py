count=0
a=1
b=2
while b<4000000:
    if(b%2==0):
        count=count+b
    a=b-a
    b=b+a
#print(b)
print(count)
    
