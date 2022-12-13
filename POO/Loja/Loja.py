from Produto import Produto
from ItemPedido import ItemPedido
from Pedido import Pedido

class Loja:
    def __init__ (self):
        self.lista_produtos = []
        self.lista_pedidos = []
    
    def cadastra_produtos (self):
        codigo = input('Digite o codigo: ')
        produto = None
        for i in self.lista_produtos:
            if i.codigo == codigo:
                produto = i

        if produto != None:
                print('Produto ja existente.')
                mudar = int(input('Digite 1 se voce deseja mudar o nome.\nDigite 2 para mudar o preco.\nDigite 3 para mudar a descricao.\nDigite 4 para mudar a quantidade.'))
                while mudar<1 and mudar>4:
                    print('Opcao invalida.')
                mudar = int(input('Digite 1 se voce deseja mudar o nome.\nDigite 2 para mudar o preco.\nDigite 3 para mudar a descricao.\nDigite 4 para mudar a quantidade.'))
                if mudar == 1:
                    i.nome = input('Digite o novo nome: ')
                elif mudar == 2:
                    i.preco_unidade = float(input('Digite o novo preco: '))
                elif mudar == 3:
                    i.descricao = input('Digite a nova descricao: ')
                elif mudar == 4:
                    i.quantidade = int(input('Digite a nova quantidade: '))
        else:
            print('Produto nao existente.')      
            preco = float(input('Digite o preço do produto desejado: '))
            nome = input('Digite o nome do produto: ')
            descricao = input('Digite a descricao do produto: ')
            quantidade = int(input('Digite a quantidade de produtos: '))
            produto = Produto(preco, codigo, nome, descricao, quantidade)
            self.lista_produtos.append(produto)

    def efetua_pedido (self):
        n = int(input('Digite a quantidade de itens desejada: '))
        lista=[]
        for i in range (n):
            codigo = int(input('Digite o codigo do produto: '))
            quantidade = int(input('Digite a quantidade: '))
            for k in self.lista_produtos:
                if codigo == k.codigo:
                    while quantidade > k.quantidade:
                        print('Estoque insuficiente.')
                        quantidade = int(input('Digite outro valor: '))
                    item = ItemPedido(k, quantidade)
                    lista.append(item)
                    k.quantidade -= quantidade
        pedido = Pedido(lista)
        self.lista_pedidos.append(pedido)

        