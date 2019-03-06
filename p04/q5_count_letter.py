def count_letter():
    word = list(input("Enter a word: ").lower())
    letter = input("Enter a letter you wish to find: " ).lower()
    count = 0
    c = []
    for j in word:
        gaps = ""
        c.append(j)
        
    
    for k in c:
            if k == letter:
                count+=1

    print("There are ",(count)," such occurences")

count_letter()
