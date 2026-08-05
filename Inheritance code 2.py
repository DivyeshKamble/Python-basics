class Animal:
    def __init__(self, species_name):
        self.species_name = species_name

    def describe(self):
        # Base method inherited by all subclasses
        print(f"Species: {self.species_name} | Role: Part of the Animal Kingdom")


class Lion(Animal):
    def __init__(self):
        # super() passes the name up to the Animal parent class
        super().__init__("Lion")

    def describe(self):
        # Method overriding: extends the base description
        super().describe()
        print("Status: King of the Jungle!")


class Cub(Lion):
    def __init__(self):
        super().__init__()
        self.species_name = "Lion Cub"

    def describe(self):
        # Inherits from Lion and Animal, but overrides with specific details
        print(f"Species: {self.species_name} | Status: Young offspring of the King!")


class FelineRelative(Animal):
    def __init__(self, relative_name="Wild Cat"):
        super().__init__(relative_name)

    def describe(self):
        super().describe()
        print("Status: Distant evolutionary cousin to the Lion.")

choices = {
    "lion": Lion(),
    "cub": Cub(),
    "cats": FelineRelative("Domestic / Wild Cat")
}

while True:
    selection = input("\nEnter choice (lion, cub, cats) or 'quit' to exit: ").strip().lower()

    if selection in choices:
        # Calls the inherited/overridden describe() method polymorphically
        choices[selection].describe()
    elif selection in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose lion, cub, cats, or quit.")