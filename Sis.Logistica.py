# Dimensão do objeto
def dimensoesobjeto():
    while True:
        try:
            alt = int(input('Digite a altura do objeto (em cm): ')) #string de pergunta sobre a altura
            comp = int(input('Digite o comprimento do objeto (em cm): ')) #string de pergunta sobre o comprimento
            lar = int(input('Digite a largura do objeto (em cm): ')) #string de pergunta sobre a largura
            vol = alt * comp * lar #calculo do volume
            print('O volume do objeto é (em cm³): {}' .format(vol)) #demonstratrivo do resultado
            if vol < 1000:
                return 10
            elif 1000 <= vol < 10000:
                return 20
            elif 10000 <= vol < 30000:
                return 30
            elif 30000 <= vol < 100000:
                return 50
            else:
                print('Não aceitamos objetos com dimensões tão grandes\nEntre com as dimensões desejadas novamente') #se o valor for maior, negara e pedira outro valor
            continue
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico\nPor favor entre com as dimensões desejadas novamente') #caso ocorra erro de digitação
            continue

#Peso do objeto
def pesoobjeto():
    while True:
        try:
            pes = int(input('Digite o peso do objeto (em kg): ')) #string de pergunta
            if pes <= 0.1:
                return 1
            elif 0.1 < pes <= 1:
                return 1.5
            elif 1 < pes <= 10:
                return 2
            elif 10 < pes <= 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados\nEntre com o peso desejado novamente') #se o valor for maior, negara e pedira outro valor
            continue
        except ValueError:
            print('Você digitou o peso do objeto com valor não numérico\nPor favor entre com o peso desejado novamente') #caso ocorra erro de digitação

            continue
#Rota do objeto
def rotaobjeto():
    while True:
        print('Selecione a rota:\nRS - De Rio de Janeiro até São Paulo\nSR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\nSB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\nRB - Rio de Janeiro até Brasília') #locais de destino
        rot = input('>> ') #string de resposta
        if rot == 'RS':
            return 1
        elif rot == 'SR':
            return 1
        elif rot == 'BS':
            return 1.2
        elif rot == 'SB':
            return 1.2
        elif rot == 'BR':
            return 1.5
        elif rot == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe!\nPor favor entre com a rota desejada novamente') #caso ocorra erro de digitaçã
        continue

#Pograma Principal
print('Bem Vindo a Companhia de Logistica Victoria Valentina Bastos Araujo S.A') #identificador pessoal

dimensao = dimensoesobjeto()
peso = pesoobjeto()
rota = rotaobjeto()
total = peso * rota * dimensao
print('Total a pagar: R${:.2f} (dimensão: {} x peso: {} x rota: {})' .format(total, dimensao, peso, rota)) #resultado final com o preço
