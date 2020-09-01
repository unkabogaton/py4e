fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('sorry file', fname, 'cannot be opened')
    exit()
count=0
for line in fhand:
    if line.startswith('2'):
        count=count+1
print('there were', count, 'lines starting in 2 in', fname)