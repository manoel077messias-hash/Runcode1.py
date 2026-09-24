nome = input().strip()
estado_civil = int(input())

if estado_civil == 1:
    conjuge = input().strip()
    total = len(nome) + len(conjuge)
else:
    total = len(nome)

print(total)



numero = input().strip()

pares = 0
for digito in numero:
    if int(digito) % 2 == 0:
        pares += 1

print(pares)



numero = input().strip()

digitos_impares = 0
for d in numero:
    if int(d) % 2 != 0:
        digitos_impares += 1

if digitos_impares == 0:
    print("Nenhum dígito é ímpar.")
elif digitos_impares == 1:
    print("Apenas um dígito é ímpar.")
else:
    print("Os dois dígitos são ímpares.")





dia = int(input())
mes = int(input())

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    print("Áries")
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print("Touro")
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
    print("Gêmeos")
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    print("Câncer")
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    print("Leão")
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    print("Virgem")
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print("Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("Escorpião")
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("Sagitário")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    print("Capricórnio")
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    print("Aquário")
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("Peixes")




a = float(input())
b = float(input())
c = float(input())

numeros = [a, b, c]
numeros.sort()

for n in numeros:
    # Se for inteiro, imprime sem casas decimais; senão imprime como float
    if n.is_integer():
        print(int(n))
    else:
        print(n)
