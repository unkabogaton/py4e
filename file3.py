fhand=open('lec.txt')
# searching a first word in each line
for line in fhand:
    line=line.rstrip()  #removing the extraspaces, the blank spaces after each line
    if line.startswith('2'):
        print(line)

#same as this..
#for line in fhand:
#    line=line.rstrip()  #removing the extraspaces, the blank spaces after each line
#    if not line.startswith('2'):
#        continue
#    print(line)

