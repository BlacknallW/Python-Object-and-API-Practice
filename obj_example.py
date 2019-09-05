class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age}"

gus = Cat("Gus", 9)

print(gus.description())

