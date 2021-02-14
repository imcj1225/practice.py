
def weight(x):
    return (x - 100) * 0.9

def BMI(x, y):
    return y / (x / 100) * 0.9
    
def program(bmi):
    if bmi < 20:
        print('저체중')
    elif 20 <= bmi < 25:
        print('정상체중')    
    elif 25 <= bmi < 30 :
        print ('경도비만') 
    elif 30 <= bmi < 40 :
        print ('비만') 
    else:
        print ('고도비만')


t = weight (150)
print(t)
a = BMI(150, 40)
print(a)
w = program(a)
