sum=0
sumofsquare=0
squareofsum=0
for i in range(1, 101):
    sum=sum+i
    sumofsquare=sumofsquare+i*i
squareofsum=sum*sum
print(squareofsum-sumofsquare)