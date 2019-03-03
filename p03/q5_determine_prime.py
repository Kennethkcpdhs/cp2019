import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(n)))
    
    #for i in range(1,20):
    #if is_prime(i)==True:
        #count = 0
        #while count<=10:
           # j = str(i)
           # j=j+" "+j
           # count+=1
       # print(j)
       # count=0
