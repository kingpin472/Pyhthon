class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, and I protect {self.city} with my {self.power} power")

    def use_power(self):
        print(f"{self.name} uses {self.power}")

# Inherited class 
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, max_altitude):
        super().__init__(name, power, city)
        self.max_altitude = max_altitude

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.max_altitude} meters")

# objects
hero1 = Superhero("Blazeman", "fire", "Metro City")
hero2 = FlyingSuperhero("SkyQueen", "wind", "Cloudville", 5000)

hero1.introduce()
hero1.use_power()
hero2.introduce()
hero2.use_power()
