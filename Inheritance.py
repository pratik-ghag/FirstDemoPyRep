class A:

    def faeture1(self):
        print("this is feature 1:")
    def faeture2(self):
        print("this is feature 2:")

class B:

    def faeture3(self):
        print("this is feature 3:")

    def faeture4(self):
        print("this is feature 4:")

class C(A,B):

    def faeture5(self):
        print("this is feature 5:")


a1 = A()
b1 = B()
c1 = C()

c1.faeture1()
c1.faeture2()
c1.faeture3()
c1.faeture4()
c1.faeture5()