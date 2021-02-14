def index(s):
    list1 = []
    list2 = []
    for i in range (len(s)):
        if i % 2 ==0:
            list1.append(s[i])
        else:
            list2.append(s[i])
    
    return list1, list2

s = input('str을 입력하시오: ')
r1, r2 = index(s)
print(r1)
print(r2)