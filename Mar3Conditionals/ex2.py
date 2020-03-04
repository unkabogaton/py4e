
hours=input("Enter Hours: ")
rate=input("Enter Rate: ")

try:
    float(hours)
    float(rate)
    if hours > 40:
        pay=(hours-40)*1.5*rate+40*rate
    else:
        pay=hours*rate
    float(pay)
    print(pay)

except:
    print("Error, please enter numeric input")
