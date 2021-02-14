f = open('hello.txt', 'a')
for i in range(11, 21):
    f.write(f'this is line {i}\n')
f.close()
