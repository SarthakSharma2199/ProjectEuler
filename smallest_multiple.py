arr=[]
for i in range (1, 21):
    isprime=1
    for j in range (2, i):
        if(i%j==0):
            isprime=0
    if(isprime):
        arr.append(i)
multiple=1
for i in arr:
    multiple=multiple*i
print(arr)
print(multiple)

for i in range (21, 1, -1):
    if(multiple%i!=0):
        multiple=multiple*i
print(multiple)

# while True:
#     flag=1
#     for i in range (1, 21):
#         if(multiple%i!=0):
#             flag=0
#     if flag==1:
#         print("found")
#         break
#     multiple=multiple+20
#     print("\n")
#     print(multiple)    
    
