class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
                self.brand = "HP"
                self.ram = "8gb"
                self.cpu ="i5"

        def show(self):
                print(self.brand, self.ram, self.cpu)


s1 = Student("Pratik", 2)
s2 = Student("Navin", 3)

s1.show()