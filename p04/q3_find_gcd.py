def return_gcd(m,n):
    if m % n == 0:
        return n
    return return_gcd(n,m%n)
