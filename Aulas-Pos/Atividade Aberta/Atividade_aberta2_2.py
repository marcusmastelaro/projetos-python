import numpy as np
matriz5x5 = np.zeros((5,5))

for linha in range(0,5):
    for coluna in range (0,5):
        dado = float(input("Digite o dado da linha %d, coluna %d: " %(linha, coluna)))    
        matriz5x5[linha][coluna] = dado

somatotal = 0
for linha in range(0,5):
    soma_linha = 0
    for coluna in range(0,5):
        soma_linha = soma_linha + matriz5x5[linha][coluna]
    print("A soma da linha %d é:" % (linha+1), (soma_linha))
    somatotal = somatotal + soma_linha
print("\nA Soma total das linhas da Matriz foi:", (somatotal))