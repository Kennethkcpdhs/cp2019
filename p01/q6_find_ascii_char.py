asciicharacter = eval(input("Input integer ascii between 0 and 127: "))
if 0<asciicharacter<127:
    print (chr(asciicharacter))
else:
    print ("Try again. Integer Ascii should be between 0 and 127.")
