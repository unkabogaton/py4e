love=['a','b','c','d']
for l in love:
    print('I love you', l)

#printing a particular content of list
print(love[3])

#length of no. of content
print(len(love))


a=[1,2,3,4]
b=[4,5,6,7]
c=a+b
print(c)

#slicing
print(c[:4])
print(c[4:])

#creating an empty list then add content
anything=list()  #creating
anything.append('anthon')   #adding
anything.append(99) 
print(anything)

#searching in list
print(8 in a)  #8 is not inside a-list so false
a.append(8) # adding 8  in a-list
print(8 in a) # this will now be true because we had added 8 in the a-list

#sorting the content of list
d=['p','j','s','f','h','s','e','a','c','b']
d.sort()  #after sorting the list, there will be new positions on it items/contents
print(d)

print(max(c)) #highest no. in list
print(min(c)) #lowest
print(len(c)) #legth or no. of content
print(sum(c)) #sum
print(sum(c)/len(c))  #ave

#input unit, using empty list

num=list() 
while True:
    line=input('Enter number here: ')
    if line == 'done':
        break
    num.append(line)
    
print(num) 
