digitinput = eval(input("Enter a number between 0 and 1000: "))
if 0<digitinput<1000: 
    digit1 = digitinput%10
    remaindigit = digitinput//10
    digit2 = remaindigit%10
    digit3 = remaindigit//10
    print ("The sum of the digits are: ", (digit1 + digit2  + digit3))

else:
    print ("your number is either too big or too small")
