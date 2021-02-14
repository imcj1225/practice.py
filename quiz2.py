def code(x):
    code = input("주민번호 앞자리를 입력하시오: ")

    year = code[:2]

    if code[0] == 0:
        year = 2000 + int(year)
        print("당신은 "+str(year)+"년 도에 태어났군요")
    else:
        year = 1900 + int(year)
        print("당신은 "+str(year)+"년 도에 태어났군요")
    
    print("당신의 생일은 "+code[2:4]+"월 "+code[4:6]+"일 이군요.")
    
    age = 2021 - year + 1
    print("당신은 올해 " + str(age) + "살 이군요.")

print(code(1))