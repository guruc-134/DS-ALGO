# getting the value of upper limit from the user
n=int(input("enter the value of n ,i.e the upper limit of the primes range\n"))

# creating a list which would contain 0's and 1's which would indicate that the number is composite or prime respectively

composites=[[[False],[0]] for i in range(n+5)]
# creaing an empty list which we will use for storing thr primes till n
prime_nums=[]

for i in range(2,n+1):
    if composites[i][0]: # if a number is composite we skip it
        continue
    prime_nums.append(i) # else we append it and then set its multiples to composite
    for j in range(i*i,n+1,i):
        composites[j][0]=[True]
        composites[j][1].append(i)
print(composites)
print(prime_nums)
