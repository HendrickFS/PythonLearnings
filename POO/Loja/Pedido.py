from Produto import Produto
from ItemPedido import ItemPedido
class Pedido:
    def __init__ (self, lista_itens):
        self.lista_itens = lista_itens
        self.total = 0
        for i in lista_itens:
            self.total += i.quantidade * i.produto.preco_unidade
    
    def __str__ (self):
        return f''