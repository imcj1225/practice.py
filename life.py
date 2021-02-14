a = ['pyhon', 'love', 'food', 'sleep']

f = open('life.txt', 'w')
f.write(f'Life is too short \n')

for i in a:
    f.write(f'you need {i} \n')

f.close()

f = open('life.txt', 'r')
f.readlines()

f.close()
