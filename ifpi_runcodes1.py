nome = input().strip()
sexo = int(input())

if sexo == 1:
    print(f'Ilmo Sr. {nome}')
elif sexo == 2:
    print(f'Ilma Sra. {nome}')



numero = int(input())

print(numero % 2 != 0)



cor = input().strip().upper()

if cor == 'V':
    print('Siga')
elif cor == 'A':
    print('Atenção')
elif cor == 'E':
    print('Pare')




caractere = input().strip()

if caractere.isdigit():
    print("número")
elif caractere.lower() in "aeiou":
    print("vogal")
elif caractere.isalpha() and caractere.lower() not in "aeiou":
    print("consoante")
else:
    print("símbolo")



n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3) / 3

if n3 > 8:
    media += 1

if media > 10:
    media = 10

print(f"{media:.2f}")


