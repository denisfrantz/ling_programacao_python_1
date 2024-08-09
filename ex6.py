cod = int(input ("código do item: "))
qntd = int(input ("quantidade do item: "))

if cod == 100:
    print ("\nvalor: R$", qntd * 1.2)
    
elif cod == 101:
    print ("\nvalor: R$", qntd * 1.3)
    
elif cod == 102:
    print ("\nvalor: R$", qntd * 1.5)
    
elif cod == 103:
    print ("\nvalor: R$", qntd * 1.2)
    
elif cod == 104:
    print ("\nvalor: R$", qntd * 1.3)
    
elif cod == 105:
    print ("\nvalor: R$", qntd * 1)
    
else:
    print ("\ncódigo inválido!")