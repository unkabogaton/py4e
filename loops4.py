#indefinite loop

num=[3,41,12,9,74,15]

#1.finding the largest num
largest = -1
for n in num:
    if n > largest:
        largest = n
print('largest is', largest)

#2.counting num components
count = 0
for n in num:
    count=count+1
print('count is', count)

#3.sum of num
sum=0
for n in num:
    sum=sum+n
print ('sum is', sum) 

#4. average of num
print('average is', sum/count)

#5.find the smallest num
smallest = None
for n in num:
    if smallest is None:
        smallest=n
    elif n < smallest:
        smallest = n
print('smallest is', smallest)

#6. search boolean variable
x=int(input('search: '))
found=False
for n in num:
    if n == int(x):
        found=True
print(found)

