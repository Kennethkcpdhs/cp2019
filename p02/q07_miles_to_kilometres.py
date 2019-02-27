a="Kilometres"
b="Miles"

km=0
print(a+"  "+b+"  "+a+"  "+b)

while km<=9:
    km+=1
    miles = km*1.609
    km2=km+10
    miles2 = km2*1.609
    print("{0}        {1:.3f}      {2}         {3:.3f}".format(km,miles,km2,miles2))
    if km==9 or km==19:
        km+=1
        miles = km*2.2
        km2=km+10
        miles2 = km2*1.609
        print("{0}        {1:.3f}      {2}         {3:.3f}".format(km,miles,km2,miles2)) 
        
