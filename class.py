
class People:
    def __init__(self, female, color):
        self.female = female
        self.color = color
        self.__age = 20

    @age.setter
    def set_age(self, value):
        self.__age == value

    def printPeople(self):
        print(f"This people is {self.color} , he age is {self.__age}, this is a {self.female} ")




people1 = People("goblin", "black")
people1.set_age(50)
people1.printPeople()
