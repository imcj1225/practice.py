class Calculator:
    num = 0

    def __init__(self, num):
        self.num = num

    def add(self, x):
        self.num += x

    def sub(self, x):
        self.num -= x
        
    def mul(self, x):
        self.num *= x

    def div(self, x):
        self.num /= x


calc1 = Calculator(10)
calc1.add(10)
print(calc1.num)

calc2 = Calculator(0)
calc2.add(7)
calc2.add(3)
calc2.sub(5)
calc2.div(2)
print(calc2.num)

calc3 = Calculator(0)
calc3.add(2)
calc3.mul(3)
calc3.sub(10)
calc3.add(8)
print(calc3.num)

