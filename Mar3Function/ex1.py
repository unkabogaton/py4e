hours=input("Enter Hours: ")
try:
    hours=float(hours)
except:
    print("Error, please enter numeric input.")
    exit()

rate=input("Enter Rate: ")
try:
    rate=float(rate)
except:
    print("Error, please enter numeric input.")
    exit()

def computepay(hours, rate):
    if hours > 40:
        return (hours-40)*1.5*rate+40*rate
    else:
        return hours*rate

x=computepay(hours,rate)
print("Your pay is " + str(x))
