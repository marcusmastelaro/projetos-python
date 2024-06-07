#definição da função
def myfunc():
    v1= "fantastico"
    print("No Escopo local, Python é " + v1)

#programa principal
v1 = "impressionante"
myfunc()
print("\nNo Escopo Global, Python é " + v1)