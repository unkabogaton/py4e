sum=0
count=0

while True:
    n=input("Enter a number: ")
    try:
        n=int(n)
    except:
        if n=='done':
            break
        else:
            print ('Invalid Input')
            continue
    sum=sum+n
    count=count+1

print(sum,count,sum/count)
