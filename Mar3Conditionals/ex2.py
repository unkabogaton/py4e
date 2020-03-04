hours=input("Enter Hours: ")
try :
    hours=float(hours)
except :
    print('Error, please enter numeric input')
 

rate = input("Enter Rate: ")
try :
    rate=float(rate)
except :
    print('Error, please enter numeric input')


if hours>40:
    pay=(hours-40)*1.5*rate+40*rate
else:
    pay=hours*rate
print(pay)