def gcd(m,n):
    gcd = 1
    
    if m % n == 0:
        return n
    
    for i in range(int(n / 2),0, -1):
        if m % i == 0 and n % i == 0:
            gcd = i
            break  
    print(i)

gcd(24,16)
gcd(255, 25)
