#definição da variavel
def myfunc():
    global x
    x = "Fantástico"

#programa principal
x = "Incrível"
myfunc()
print("Python é " + x)