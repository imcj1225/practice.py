def fit(cm):
    return (cm-100) * 0.9

def bmi(kg, cm):
   return kg / (cm/100) ** 2

def per(bmi):
    result = ''
    if bmi < 20:
        print ('저체중')
    elif bmi >= 20 and bmi < 30:
        print ('경도비만')
    elif bmi >=30 and bmi < 40:
        print ('비만')
    elif bmi >=40:
        print ('고도비만')
    return result


print (fit(cm))
print (bmi(kg))
print (per(bmi))