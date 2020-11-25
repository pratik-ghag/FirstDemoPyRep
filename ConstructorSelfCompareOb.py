class Computer:

    def __init__(self):
        self.name = "pratik"
        self.age = 23

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.name = "Navin"
c1.age = 21
c2 = Computer()

if c1.compare(c2):
    print("Age is Same:")
else:
    print("Age is different:")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)