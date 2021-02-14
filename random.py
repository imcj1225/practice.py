import random
def listm(l):
    return random.choice(l) * random.randint(1,100)

x = listm([1,2,3,4])
print (x)
