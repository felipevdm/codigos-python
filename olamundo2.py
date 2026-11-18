print('Ola mundo')
print('Como te atopas?')

print('Los 10 primeros números primos son:')

numero = 2
encontrados = 0

while encontrados < 10:
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        print(numero)
        encontrados += 1

    numero += 1
