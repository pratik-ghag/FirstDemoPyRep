class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def add(self):
        pass

    def config(self):
        print("Config is:", self.cpu, self.ram)


comp1 = Computer('i5', 8)
comp2 = Computer('i3', 16)

# this is how it works
# computer.config(comp1)
# computer.config(comp2)

#  this is how we use
comp1.config()
comp2.config()
