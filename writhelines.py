f = open('hello.txt', 'w')

for i in range(1, 11):
    f.write(f'this is line {i}\n')

f.close()

