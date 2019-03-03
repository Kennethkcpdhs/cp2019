def display_pattern(num):
    
    count = 1
    listss = []
    while count <= num:
        listss.append(str(count))
        b = listss[::-1]
        c = " ".join(b)
        print("{0:>8}".format(c))
        count += 1
