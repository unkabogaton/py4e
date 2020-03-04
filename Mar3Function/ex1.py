
hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
def computepay(hours, rate):
    if hours > 40:
        pay=(hours-40)*1.5*rate+40*rate
    else:
        pay=hours*rate
    return pay
x=computepay(hours,rate)
print("Your pay is " + str(x))
