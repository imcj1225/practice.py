def gugudan(x):
    list = []
    for i in range(1,10):
        list.append(x * i)
    return list
x = int(input('몇 단?: '))

print(gugudan(x))
