#armazena a quantidade de segundos informada pelo usuario
segundos = int(input("informe a quantidade de segundos a ser transformada: "))

#faz as devidas conversoes para horas e minitos, guardando o que restar de segundos
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

#informa as quantidades ao usuario
print(f"{segundos} segundos é igual a: \n{horas} horas\n{minutos} minutos\ne restam {segundos_restantes} segundos")