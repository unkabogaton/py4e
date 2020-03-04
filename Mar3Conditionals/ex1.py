
hours=float(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
if hours > 40:
    pay=(hours-40)*1.5*rate+40*rate
else:
    pay=hours*rate
print(pay)
