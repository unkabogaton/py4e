fruit="anthon"

print(fruit[0])   #locating positions using index.  a-0 n-1 t-2 h-3 o-4 n-5

x=len(fruit)  #look for length of string
print(x)

index=0             #printing the index of letters in strings
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1

for letter in fruit:
    print(letter)


#slicing string
s="Anthon Ralph Dela Torre"
print(s[0:6])   #including only Anthon
print(s[18:])   #includiiing only Torre

print(fruit+" "+s) # ' ' - puting space when joining 2 strings

#lowercase
print(s.lower())

#uppercase
print(s.upper())

#searching specific phrase or part of string
pos = s.find('re') #this show that the 're' is in the index 21
print(pos)

#replacing a part of string
print(s.replace('Anthon', 'Anthonietta'))

#removing extraspaces in left and right of the whole string
print(s.strip())

#query what is the starting of the string, True or False
print(s.startswith('A'))
print(s.startswith('a'))

