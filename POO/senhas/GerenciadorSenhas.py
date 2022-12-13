class GerenciadorSenhas:
    def __init__(self, senhas):
        self.senhas = senhas

    def get_senha(self):
        return self.senhas[-1]

    def set_senha(self, novaSenha):
        if novaSenha not in self.senhas:
            self.senhas.append(novaSenha)
        else:
            print('Senha já existente')
    
    def is_correta(self, tentativa):
        if self.senhas[-1] == tentativa:
            return True
        else:
            return False

    
    