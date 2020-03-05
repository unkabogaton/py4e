
largest = None
smallest = None
while True:
    n=input('Enter a number: ')
    try:
        value=int(n)
    except:
        if n=='done':
            break
        else:
            print ('Invalid Input')
            continue
    if largest is None:
            largest=value
    elif value > largest:
        largest = value
    if smallest is None:
        smallest = value
    elif value < smallest:
        largest=value
print ("largest number: " + str(largest))
print ("smallest number: " + str(smallest))
