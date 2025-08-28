class ProgrammingLanguage:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator

    def describe(self):
        print(f"{self.name} was created by {self.creator}.")

    def run(self):
        print(f"{self.name} is running code...")

class CompiledLanguage(ProgrammingLanguage):
    def run(self):
        print(f"{self.name} compiles code before running.")

class InterpretedLanguage(ProgrammingLanguage):
    def run(self):
        print(f"{self.name} interprets code line by line.")

# Example usage
python = InterpretedLanguage("Python", "Guido van Rossum")
cpp = CompiledLanguage("C++", "Bjarne Stroustrup")

python.describe()
python.run()

cpp.describe()
cpp.run()