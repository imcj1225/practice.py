def introduce(name, age, score):
    print(f'name: {name}, age: {age}, score: {score}')

name = input('name: ')
age = input('age: ')
score = input('score: ')

introduce(name, age, score)


def profile(n,a,s):
    return f'name: {n}, age: {a}, score: {s}'

x = profile('harry', 12, 80)
print(x)

