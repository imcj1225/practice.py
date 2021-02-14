money = True
amount = 300

if money and amount >=3000:
    print('택시타')
elif money and amount <3000:
    print('버스타')
elif not money and amount == 0:
    print('걸어가')



if money:
    if amount >= 3000:
        print ('taxi')
    else:
        print('bus')
else:
    print ('walk')

