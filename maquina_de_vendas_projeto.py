import time

pagador = 0
preco = 0
troc = 0
matrizvalor = 0
valortroco = 0
troco = 0
fim_valor = 1

quantcedulas = [
    ['R$50', 'R$10', 'R$2', 'R$1', 'R$0,50', 'R$0,10', 'R$0,05', 'R$0,01'],
    [5, 12, 15, 13, 22, 23, 17, 12],
    [50, 10, 2, 1, 0.5, 0.1, 0.05, 0.01],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

maquina = [
    [1, 'Coca-Cola', 3.75, 2],
    [2, 'Pepsi', 3.76, 5],
    [3, 'Monster', 9.96, 1],
    [4, 'Café', 1.25, 100],
    [5, 'Redbull', 13.99, 2]
]

def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def imprimir_itens(matriz_itens):
    matriz_itens = []
    for linha in range(len(maquina)):
        matriz_itens.append([])
        for coluna in range(1):
            matriz_itens[linha].append(maquina[linha][0])
            matriz_itens[linha].append(maquina[linha][1])
        print(f'{maquina[linha][0]} - {maquina[linha][1]}')

print("Bem vindo a Máquina de Compras!")
escolha_adm = str(input("Deseja entrar no modo administrador? "))
if escolha_adm == 'Sim' or escolha_adm == 'sim' or escolha_adm == 'SIM':
    contador_adm = 0
    fim_adm = 1
    print("Você entrou no modo administrador!")
    while contador_adm < fim_adm:
        print_matriz(maquina)
        opcoes_adm = int(input("1 - Cadastrar um produto\n2 - Alterar um produto\n3 - Remover um produto\nO que você deseja fazer: "))
        if opcoes_adm == 1:
            produto_novo = []
            produto_novo.append(len(maquina)+1)
            produto_novo.append(str(input("Entre com o nome do produto: ")))
            produto_novo.append((float(input("Entre com o valor do produto: "))))
            produto_novo.append((int(input("Entre com o estoque do produto: "))))
            maquina.append(produto_novo)
            print_matriz(maquina)
        if opcoes_adm == 2:
            id_alterar = (int(input("Entre com o ID do produto que você deseja alterar: ")))
            id_alterar = id_alterar - 1
            maquina[id_alterar][1] = str(input("Entre com o nome do produto: "))
            maquina[id_alterar][2] = float(input("Entre com o valor do produto: "))
            maquina[id_alterar][3] = int(input("Entre com o estoque do produto: "))
            print_matriz(maquina)
        if opcoes_adm == 3:
            id_remove = (int(input("Entre com o ID do produto que você deseja remover: ")))
            id_remove = id_remove - 1
            del maquina[id_remove]
            for i in range(id_remove, len(maquina)):
                maquina[i][0] = maquina[i][0] - 1
            print_matriz(maquina)
        if opcoes_adm != 1 and opcoes_adm != 2 and opcoes_adm != 3:
            print("Opção inválida.")
        opcoes_contador_adm = str(input("Deseja continuar no modo administrador? "))
        if opcoes_contador_adm == 'Sim' or opcoes_contador_adm == 'sim' or opcoes_contador_adm == 'SIM':
            fim_adm += 1
            contador_adm += 1
        else:
            contador_adm += 1
            print("Ok. Continue a comprar!")

else:
    print("Continue a comprar!")

contador_maquina = 0
fim_maquina = 1

while contador_maquina < fim_maquina:
    itens = []
    imprimir_itens(itens)
    id = int(input('Entre com o ID do Item que você deseja: '))
    id = id - 1
    preco = maquina[id][2]
    produto = maquina[id][1]
    quantidade = maquina[id][3]
    if quantidade > 0:
        print(f"O valor do(a) {produto} é: R${preco}")
        contador_valor = 0
        fim_valor = 1
        while contador_valor < fim_valor:
            pagador = float(input("Entre com o valor para pagar: "))
            if pagador >= preco:
                print("Obrigado por comprar!")
                troc = pagador - preco
                troco = troc
                for i in range(0, 7):
                    if troc > quantcedulas[2][i]:
                        quantcedulas[3][i] = troc // quantcedulas[2][i]
                        troc = troc - quantcedulas[3][i] * quantcedulas[2][i]
                        if troc < 0.05:
                            if troc + 0.01 > 0.05:
                                quantcedulas[3][6] = 1
                            elif troc + 0.02 > 0.05:
                                quantcedulas[3][7] = 4
                            elif troc + 0.03 > 0.05:
                                quantcedulas[3][7] = 3
                            elif troc + 0.04 > 0.05:
                                quantcedulas[3][7] = 2
                            else:
                                quantcedulas[3][7] = 1
                for i in range(0, 7):
                    quantcedulas[1][i] = quantcedulas[1][i] - quantcedulas[3][i]
                if troco > 0:
                    if quantcedulas[1][0] < 1 or quantcedulas[1][1] < 1 or quantcedulas[1][2] < 1 or quantcedulas[1][3] < 1 or quantcedulas[1][4] < 1 or quantcedulas[1][5] < 1 or quantcedulas[1][6] < 1 or quantcedulas[1][7] < 1:
                        time.sleep(1.5)
                        print('A compra precisou ser cancelada devido à falta de troco.')
                        contador_maquina += 1
                        contador_valor += 1
                    else:
                        print(f'Seu troco é de R${troco :.2f}, e as cédulas recebidas serão:\n {quantcedulas[3][0] :.0f} Nota(s) de R$50\n {quantcedulas[3][1] :.0f} Nota(s) de R$10\n {quantcedulas[3][2] :.0f} Nota(s) de R$2\n {quantcedulas[3][3] :.0f} Moeda(s) de R$1\n {quantcedulas[3][4] :.0f} Moeda(s) de R$0,50\n {quantcedulas[3][5] :.0f} Moeda(s) de R$0,10\n {quantcedulas[3][6] :.0f} Moeda(s) de R$0,05\n {quantcedulas[3][7] :.0f} Moeda(s) de R$0,01')
                        print(f'\nO estoque de cédulas é {quantcedulas[1][0] :.0f} notas de R$50, {quantcedulas[1][1] :.0f} notas de R$10, {quantcedulas[1][2] :.0f} notas de R$2, {quantcedulas[1][3] :.0f} moedas de R$1, {quantcedulas[1][4] :.0f} moedas de R$0,50, {quantcedulas[1][5] :.0f} moedas de R$0,10, {quantcedulas[1][6] :.0f} moedas de R$0,05, {quantcedulas[1][7] :.0f} moedas de R$0,01.')
                        maquina[id][3] = quantidade - 1
                        contador_valor += 1
                else:
                    contador_maquina += 1
                    contador_valor += 1
            else:
                print("O valor inserido não alcançou o valor do produto! Tente novamente")
                fim_valor += 1
    contador_maquina += 1



