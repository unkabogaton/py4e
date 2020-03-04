count=0
sum=0
num=''

while(num!="done"):
    input("Enter number here: ")
    try:
        num = int(num)
    except:
        print("bad data")
        continue
    sum = sum + num
    count = count + 1
print (sum, count, sum/count)
