side1 = eval(input("Enter side 1: "))
side2 = eval(input("Enter side 2: "))
side3 = eval(input("Enter side 3: "))
if (side1+side2)>side3 or (side2+side3)>side1 or (side1+side3)>side2:
    print (side1+side2+side3)
else:
    print ("Invalid triangle!")
