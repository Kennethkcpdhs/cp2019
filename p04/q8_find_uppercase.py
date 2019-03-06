def find_num_uppercase():
    word = list(input("Enter a word: "))
    count = 0
    c = []
    for j in word:
        gaps = ""
        c.append(j)
        
    for i in c:
        if (i.isupper()):
            count+=1

    print("There are ",(count)," such occurences of uppercase")

find_num_uppercase()
