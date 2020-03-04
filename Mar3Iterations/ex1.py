sum=0
count=0

while True:
    try:
        n=input("Enter a number: ")
        if (n=="done"): 
            break
        n=int(n)
        sum=sum+n
        count=count+1
    except:
        print("Invalid input")
print (sum, count, sum/count)