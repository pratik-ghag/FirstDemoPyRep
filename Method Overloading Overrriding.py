# overloading using @ decortors

# using default parameters in method
#  and calling method with less arguemts
class Student:

    def sum(self,a = 0 ,b = 0, c = 0):
        s = (a + b + c)
        return s
s1 = Student()

print(s1.sum(5,78))
# method overrriding
# class Student1:
#
#     def cal_marks(self,m1,m2,m3):
#         print(m1 + m2 + m3)
#
# class Student2(Student1):
#
#     def cal_marks(self,m1,m2):
#
#         print(m1 + m2)
#
# s1 = Student1()
#
# s1.cal_marks(25,52,42)