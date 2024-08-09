diasTrabalhados = int(input ("quantidade de dias trabalhados: "))

valorTotal = diasTrabalhados * 20

print ("\nvalor bruto: R$", float(valorTotal))
print ("valor líquido: R$", float(valorTotal - (valorTotal * 0.08)))