def find_largest():
    number = (input("Enter a number: "))
    listofnum = []
    for i in number.strip():
        listofnum.append(i)
    listofnum.sort()
    print(listofnum[-1])
    

   
find_largest()
