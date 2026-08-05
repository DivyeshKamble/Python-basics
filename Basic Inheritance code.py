class Animal:

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        return "Some generic animal sound"


class Cat(Animal):

    def __init__(self, name: str, indoor: bool = True):
        super().__init__(name, species="Felis catus")
        self.indoor = indoor

    def make_sound(self) -> str:
        return "Meow!"

    def purr(self) -> str:
        return f"{self.name} is purring contentedly."


class Lion(Animal):

    def __init__(self, name: str, pride_size: int = 5):
        super().__init__(name, species="Panthera leo")
        self.pride_size = pride_size

    def make_sound(self) -> str:
        return "ROAR!"

    def hunt(self) -> str:
        return f"{self.name} is hunting with the pride."


class Cub(Lion):

    def __init__(self, name: str, age_months: int):
        # Cubs inherit pride size or start in the same family line
        super().__init__(name, pride_size=1)
        self.age_months = age_months

    def make_sound(self) -> str:
        # Overriding sound for a younger, high-pitched roar
        return "Squeaky miniature roar!"

    def play(self) -> str:
        return f"{self.name} is pouncing on its siblings."


#Usage Example
if __name__ == "__main__":
    whiskers = Cat(name="Whiskers")
    print(f"{whiskers.name} ({whiskers.species}): {whiskers.make_sound()}")
    print(whiskers.purr())

    print("---")

    # Lion Family
    simba_parent = Lion(name="Mufasa", pride_size=12)
    print(
        f"{simba_parent.name} ({simba_parent.species}): {simba_parent.make_sound()}"
    )
    print(simba_parent.hunt())

    print("---")

    # Cub (inherits Lion properties)
    simba_cub = Cub(name="Simba", age_months=4)
    print(f"{simba_cub.name} ({simba_cub.species}): {simba_cub.make_sound()}")
    print(simba_cub.play())