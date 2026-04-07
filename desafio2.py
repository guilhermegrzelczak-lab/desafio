#guarda o numero que o usuario informar
numero = int(input('diga o numero para verificar se é par ou impar'))

#verifica se o resto do numero dividido por 2 e igual a zero
if numero % 2 == 0:
    print(f"{numero} é par") #se sim, retorna que é par
else:
    print(f"{numero} é impar") #se nao, é impar