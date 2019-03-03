def reverse_int():
      d =[]
      n = str(input("Enter a number: "))
      for i in n:
            d.append(i)
      d = d[::-1]

      e = ''.join(d)
      print(e)
      

reverse_int()
