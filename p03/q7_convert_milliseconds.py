import math
def convert_ms():
    n = int(input("Enter number of milliseconds to convert: "))
    hours = round((n/(1000*60*60))%60)
    minutes = round((n/(1000*60))%60)
    seconds = round((n/1000)%60)
    print((hours),":",(minutes),":",(seconds))


convert_ms()
