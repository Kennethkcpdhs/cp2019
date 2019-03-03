def find_factors(number):
      factors = []
      for i in range(2,number):
            while number%i == 0:
                  factors.append(i)
                  number = number//i
                             
      factors.sort()
      
      print("The smallest divisors are: ",(factors))


number = eval(input("Enter a number: "))
find_factors(number)
