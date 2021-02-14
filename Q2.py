a = input("주민번호 앞자리를 입력하시오: ")

a1 = a[0:2]
a2 = a[2:4]
a3 = a[4:6]

if a1[0] == '0':
    year = 2000 + int(a1)
else:
    year = 1900 + int(a1)
   

print ('당신은' + str(year) + '년도에 태어났군요.')
print ('당신의 생일은 ' + a2 + '월 ' + a3 + '일 이군요.')

age = 2021 - year + 1
print ('당신은 올해 ' + str(age) + '살 이군요.' )