#solicita qual opcao de conta o usuario quer fazer e armazena
opcao = int(input("qual operação quer fazer\n 1-Adiçao\n 2-Subtração\n 3-Divisão\n 4-Multiplacação\n "))

#solicita os numeros que sera feita a conta
num1 = int(input("primeiro numero: "))
num2 = int(input("segundo numero: "))

#com base na opcao selecionada, decide pelas condicoes qual operacao realizar
if opcao == 1:
    print(f"soma = {num1 + num2}")
elif opcao == 2:
    print(f"subtração = {num1 - num2}")
elif opcao == 3:
    print(f"divisão = {num1 / num2}")
elif opcao == 4:
    print(f"multiplicação = {num2 * num1}")
else:
    print("opcao invalida") #se nao for nenhuma das opcoes possiveis, informa o erro
