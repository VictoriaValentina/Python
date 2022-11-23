cdepecas = [] #lista global vazia


# #Cadastro de Peças
def cadastrarpecas(codigo):
    print('Você selecionou a opção de Cadastrar Peça')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Por favor entre com o NOME da peça: ')
    fab = input('Por favor entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor entre com o VALOR da peça: '))
    dicionarioPecas = {'Codigo': codigo,
                       'Nome': nome,
                       'Fabricante': fab,
                       'Valor': valor}
    cdepecas.append(dicionarioPecas.copy())


def consultarpeca():
    while True:
        try:
            print('Você selecionou a opção de Consultar Peças')
            opcao2 = (int(input('Escolha a opção desejada: \n'
                                '1-Consultar Todas as Peças\n'
                                '2-Consultar Peças por Código\n'
                                '3-Consultar Peças por Fabricante\n'
                                '4-Retornar\n'
                                '>> ')))
            if opcao2 == 1:
                print('Você selecionou a opção Consultar Todas as Peças')
                print('_' * 10)
                for objeto in cdepecas:  # selecionar dicionarios da lista
                    for key, value in objeto.items():
                        print('{} : {}'.format(key, value))
            elif opcao2 == 2:
                print('Você selecionou a opção Consultar Peças por Código')
                print('_' * 10)
                cod = int(input('Digite o CÓDIGO da Peça: '))
                for objeto in cdepecas:
                    if objeto['Codigo'] == cod:
                        for key, value in objeto.items():
                            print('{} : {}'.format(key, value))
            elif opcao2 == 3:
                print('Você selecionou a opção Consultar Peças por Fabricante')
                print('_' * 10)
                fabr = input('Digite o FABRICANTE da Peça: ')
                for objeto in cdepecas:
                    if objeto['Fabricante'] == fabr:
                        for key, value in objeto.items():
                            print('{} : {}'.format(key, value))
            elif opcao2 == 4:
                print('Finalizando!')
                return
            else:
                print('Opção inválida!')
                continue
        except ValueError:
            print('Valor não numérico!')

def removerPeca():
    print('Você selecionou a opção de remover peças')
    codi = int(input('Digite o codigo da peça a ser removida: '))
    for peca in cdepecas:
        if peca['Codigo'] == codi:
            cdepecas.remove(peca)


# Programa Principal


print('Bem Vindo ao Controle de Estoque da Bicicletaria da Victória Valentina Bastos Araújo')
codigop = 0

while True:
    try:
        opcao = (int(input('Escolha a opção desejada: \n'
                           '1-Cadastrar peças\n'
                           '2-Consultar peças\n'
                           '3-Remover peças\n'
                           '4-Sair\n'
                           '>> ')))
        if opcao == 1:
            codigop += 1
            cadastrarpecas(codigop)
        elif opcao == 2:
            consultarpeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Finalizando Programa!')
            break
        else:
            print('Opção inválida!')
            continue
    except ValueError:
        print('Valor não numérico!')
