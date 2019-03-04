def sum_series1(i):
    count = 1
    m = (1/count)
    while count<=i:
        m+=(1/count)
        count+=1
    return m
