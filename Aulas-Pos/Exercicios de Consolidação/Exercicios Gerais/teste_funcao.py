# definição da função
def describe_pet(animal_type, pet_name):
    """Imprime informações sobre o animal de estimação"""
    print(f"\nEu tenho um {animal_type}.")
    print(f"Meu {animal_type} se chama {pet_name.title()}.")

#função é chamada 2 vezes com parametros diferentes
describe_pet('Cachorro', 'Bebe')
describe_pet('Cachorro','Puppy')