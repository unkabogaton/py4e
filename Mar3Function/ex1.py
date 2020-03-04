
hours=float(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
def computepay(hours, rate):
    if hours > 40:
        return (hours-40)*1.5*rate+40*rate
    else:
        return hours*rate

x=computepay(hours,rate)
print("Your pay is " + str(x))
