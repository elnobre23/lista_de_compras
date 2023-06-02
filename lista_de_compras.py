import os

lista_de_compra = []
opcoes = ('i', 'a', 'l', 's')

while True:
    opcao = input('Selecione uma opção:\n[i]nserir, [a]pagar, [l]istar ou [s]air: ' ).lower()
    if opcao in opcoes:

        if opcao == opcoes[0]:
            adicionar_compra = input('Adicione um item: ')
            lista_de_compra.append(adicionar_compra)

        elif opcao == opcoes[1]:
            i = int(input('Selecione um índice para apagar: '))
            try:
                apagar_compra = lista_de_compra.pop(i)
            except IndexError:
                print('Não foi possível apagar esse índice.')
                continue
        elif opcao == opcoes[2]:
            for indice, item in enumerate(lista_de_compra):
                print(indice, item)
        else:
            os.system('cls')
            lista_de_compra = []      
    else:
        print('Digite uma opção válida!')
