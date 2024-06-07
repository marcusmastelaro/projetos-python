class Dog:
    """modelagem do animal cachorro"""
    def __init__(self, name, age):
        """inicializa os atributos name e age"""
        self.name = name
        self.age = age
    def sit(self):
        """Simula cachorro atendendo ao comando de sentar"""
        print(f"{self.name} está sentado!")
    def roll_over(self):
        """Simula o cachorro atendendo ao comando de rolar"""
        print(f"{self.name} rolou!")