a="Kilograms"
b="Pounds"
kg = 0
print(a+"  "+b)

while kg<=9:
    kg+=1
    pounds = kg*2.2
    print("{0}        {1:.2f}".format(kg,pounds))
    if kg==9:
        kg+=1
        pounds = kg*2.2
        print("{0}       {1:.2f}".format(kg,pounds))
    



