#class student

class Student:
    name = ''
    korean = 0
    english = 0
    math = 0

    def __init__ (self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def sum_score(self):
        return sum([self.korean, self.english, self.math])

    def avg(self):
        return self.sum_score() / 3
    

s1 = Student('Kim', 90, 80, 60)
s2 = Student('Lim', 70, 60, 90)
s3 = Student('Lee', 100, 70, 30)
s4 = Student('Park', 80, 40, 80)

print(max(s1.avg(), s2.avg(), s3.avg(), s4.avg()))
print((s1.korean + s2.korean + s3.korean + s4.korean)/4)