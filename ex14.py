duracaoChamada = float(input ("duração da chamada telefônica (em minutos): "))

if duracaoChamada < 3:
    custo = 1.15
    
else:
    custo = ((duracaoChamada - 3) * 0.26) + 1.15

print("\ncusto da chamada: R$", custo)