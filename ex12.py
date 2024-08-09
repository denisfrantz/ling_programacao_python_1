def gCgF (tc):
    tf = (9 / 5) * tc + 32
    
    return tf

def gFgC (tf):
    tc = (5 / 9) * (tf - 32)
    
    return tc

opcao = int(input ("1) converter graus C para graus F\n2) converter graus F para graus C\n\n"))

if opcao == 1:
    tc = float(input ("\ntemperatura em graus C: "))
    print ("temperatura em graus F: ", round(gCgF(tc), 2))
    
elif opcao == 2:
    tf = float(input ("\ntemperatura em graus F: "))
    print ("temperatura em graus C: ", round(gFgC(tf), 2))
    
else:
    print ("\nopção inválida!")