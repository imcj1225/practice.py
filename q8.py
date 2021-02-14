import math

def cal(a):
    a = [-8, 2, 7, 5, -3, 5, 0, 1]
    return sum (a), sum(a)/len(a), max(a), min(a)

sum, avg, max, min = cal(a)

print(sum)
print(avg)
print(max)
print(min)    