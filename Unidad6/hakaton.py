texto = input("Introduce un texto para analizar: ")
bocales = 0
consonantes = 0
numeros = 0
otros = 0

for caracter in texto:
    caracter = caracter.lower()
    
    if caracter in ['a', 'e', 'i', 'o', 'u']:
        bocales += 1
    elif 'a' <= caracter <= 'z':
        consonantes += 1
    elif '0' <= caracter <= '9':
        numeros += 1
    else:
        otros += 1

print("bocales:", bocales)
print("Consonantes:", consonantes)
print("Numeros:", numeros)
print("Otros caracteres:", otros)
