def sum_series1(i):
    count = 0
    m = (count/((2*count)+1))
    while count<=i:
        m+=(count/((2*count)+1))
        count+=1
        
    return m
