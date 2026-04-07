# armazena o valor inicial, a taxa de juros e o tempo em anos
valorInicial = float(input("informe o valor inicial: "))
taxaDeJuros = float(input("informe a taxa de juros (ao ano): "))
anos = float(input("informe o tempo em anos: "))

#calcula os juros
juros = (valorInicial * taxaDeJuros * anos) / 100

#informa o total de juros e o valor final que ficara
print(f"os juros serao de {juros} e o valor final sera {valorInicial + juros}")