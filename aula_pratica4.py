ingressos = int(input('Ingressos à serem vendidos: '))
print('')

total = 0
soma_idades = 0
valor = 0
pessoas = 0

for i in range(0, ingressos):
    idade = int(input(f'Quantidade: {ingressos - i} | Digite a idade do cliente?: (0 - encerra a contagem)'))

    if idade < 3 and idade > 0:
        valor = 0.00
        pessoas += 1

    elif idade >= 3 and idade <= 12:
        valor = 15.00
        pessoas += 1

    elif idade > 12:
        valor = 30.00
        pessoas += 1

    if idade == 0:
        break

    total += valor
    soma_idades += idade



print(f'\nO valor total arrecadado foi R${total:.2f}\n{pessoas} pessoas compraram o ingresso.\nA média das idades das pessoas foi {soma_idades/pessoas}')
