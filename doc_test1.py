
with open('song2.bak','w+') as f:
    for line in f:
        print(line.strip())
    f.write('Hello')
