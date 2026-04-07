# cria a variavel que vai armazenar os nomes
nomes = []
#repeticao para pedir 5 nomes ao usuario
for i in range(5):
    #salva os nomes na variavel criada acima
    nomes.append(input(f"diga o nome {i + 1}: "))

print('lista de nomes: ')
# nova repeticao para listar os nomes
for nome in nomes:
    print(nome)

