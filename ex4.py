tempo = int(input ("duração de um evento (em segundos): "))

print ("\nhora(s): ", tempo // 3600)
print ("minuto(s): ", (tempo % 3600) // 60)
print ("segundo(s): ", (tempo % 3600) % 60)