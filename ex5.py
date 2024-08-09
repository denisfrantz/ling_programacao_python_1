idade = int(input ("idade do nadador: "))

if idade >= 18:
    print ("\ncategoria: adulto")
    
elif idade >= 14:
    print ("\ncategoria: juvenil B")
    
elif idade >= 11:
    print ("\ncategoria: juvenil A")
    
elif idade >= 8:
    print ("\ncategoria: infantil B")
    
elif idade >= 5:
    print ("\ncategoria: infantil A")
    
else:
    print ("\nsem categoria")