entrada = input('digite a hora ')
hora = int(entrada)
if hora >= 0 and hora <= 11:
    print("bom dia")
elif hora >= 12 and hora <= 17:
    print("boa tarde")
else:
    print("boa noite")