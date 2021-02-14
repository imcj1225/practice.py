class car:
    color = ''
    speed = 0

    def upSpeed(self, val):
        self.speed += val

    def downSpeed(self, val):
        self.speed -= val
    
    def stop(self):
        self.speed = 0


myCar = Car()

myCar.color = "White"
myCar.speed = 50
print(myCar.speed)
print(f'car1의 현재 속도는 {myCar.speed}')

myCar.upSpeed(20)
print(myCar.speed)
print(f'car1의 현재 속도는 {myCar.speed}')