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

if hours > 40:
    print((hours-40)*1.5*rate+40*rate)
else:
    print(hours*rate)
