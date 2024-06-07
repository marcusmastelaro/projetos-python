class Car:
    """modelagem de carro através de carro"""
    def __init__(self, make, model, year):
        """inicializa os atributos que descrevem carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna o nome descritivo para carro"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Imprime a distancia percorrida pelo carro"""
        print(f"Esse carro rodou {self.odometer_reading} KMs.")

    def update_odometer(self, kilometragem):
        """Atualiza valor do odometro para valor fornecido"""
        self.odometer_reading = kilometragem

    def increment_odometer(self, kms):
        """incrementa o odometro com valor fornecido"""
        self.odometer_reading += kms
        