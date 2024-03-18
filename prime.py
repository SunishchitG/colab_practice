N = 100
prime = []
def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True  
for i in range(2,N):
    if prime_number(i):
        prime.append(i)
    else:
        continue    
print (prime)    

