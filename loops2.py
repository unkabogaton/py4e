#indefinite loop.  'while'-loop
while True:
    line=input('type .done. to stop printing: ') #for the input

    if line[0] == '#':      #didnt print the word starting in hashtag
        continue
    if line == 'done':
        break
    print (line)

print('Done!')