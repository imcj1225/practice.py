def list_print(l):
    sum = 0
    for i in l:
        sum += i
    return sum, len(l), sum / len(l)

x = list_print([1,2,3,4,5])
print(x)

