print('Bem Vindo a Lanchonete da Victoria Valentina Bastos Araujo') #identificador pessoal
print('***************Cardápio***************')
print('| Código |       Descrição       | Valor |')
print('|  100   |    Cachorro Quente    |  9,00 |')
print('|  101   | Cachorro Quente Duplo | 11,00 |')
print('|  102   |        X-Egg          | 12,00 |')
print('|  103   |       X-Salada        | 12,00 |')
print('|  104   |       X-Bacon         | 14,00 |')
print('|  105   |        X-Tudo         | 17,00 |')
print('|  200   |   Refrigerante Lata   |  5,00 |')
print('|  201   |      Chá Gelado       |  4,00 |')

total = 0 #inicio da contagem para o total do valor

while True: #inicio do loop
    cod = (input('Entre com o código desejado: ')) #sting de pergunta

#codigos e seus respectivos valores, assim como a variavel acumuladora
    if cod == '100':
        valor = 9.00
        total += valor
        print('Você pediu um Cachorro Quente no valor de R${:.2f}'.format(valor))
    elif cod == '101':
        valor = 11.00
        total += valor
        print('Você pediu um Cachorro Quente Duplo no valor de R${:.2f}'.format(valor))
    elif cod == '102':
        valor = 12.00
        total += valor
        print('Você pediu um X-Egg no valor de R${:.2f}'.format(valor))
    elif cod == '103':
        valor = 12.00
        total += valor
        print('Você pediu um X-Salada no valor de R${:.2f}'.format(valor))
    elif cod == '104':
        valor = 14.00
        total += valor
        print('Você pediu um X-Bacon no valor de R${:.2f}'.format(valor))
    elif cod == '105':
        valor = 17.00
        total += valor
        print('Você pediu um X-Tudo no valor de R${:.2f}'.format(valor))
    elif cod == '200':
        valor = 5.00
        total += valor
        print('Você pediu um Refrigerante Lata no valor de R${:.2f}'.format(valor))
    elif cod == '201':
        valor = 4.00
        total += valor
        print('Você pediu um Chá Gelado no valor de R${:.2f}'.format(valor))
    else:
        print('Opção Inválida!') #ao digitar o codigo incorreto, voltará ao menu inicial
        continue

    print('Deseja pedir mais alguma coisa?') #pergunta acumulativa
    print('1 - SIM')
    print('2 - NÃO')

    opcao = input('R: ')
    if opcao == '1': #se a resposta for SIM, voltara ao menu inicial
        continue
    elif opcao == '2': #se a resposta for NÃO, o valor total é calculado e o loop encerrado
        print('O total a ser pago é: R${:.2f}'.format(total))
        break