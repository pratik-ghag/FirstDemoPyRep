class Student:

    schoolName = "MU"
    def __init__(self,m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschoolname(cls):
        return cls.schoolName

    @staticmethod
    def info():
        print("This is school:")


s1 = Student(10, 20, 30)
s2 = Student(15, 30, 45)

print(s1.avg())
print(s2.avg())
print(Student.getschoolname())
