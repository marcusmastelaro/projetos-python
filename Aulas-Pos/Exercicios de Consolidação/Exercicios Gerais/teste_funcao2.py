def repeatStr(mytext, text_lenght):
    s = ''
    for i in range(0, text_lenght):
        s = s + mytext
    return s

#chamada da função
output = repeatStr('->-<',5)

print(output)