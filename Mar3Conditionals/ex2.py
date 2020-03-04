hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
try:
    hours=float(hours)
    rate=float(rate)
except:
    print("Error, please enter numeric input.")
    exit()

if hours > 40:
    print((hours-40)*1.5*rate+40*rate)
else:
    print(hours*rate)
