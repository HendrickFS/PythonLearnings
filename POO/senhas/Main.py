from GerenciadorSenhas import GerenciadorSenhas

gerenciador1 = GerenciadorSenhas(["senha1", "senha2", "12345678"])
gerenciador2 = GerenciadorSenhas(["123"])

print(gerenciador1.get_senha())

gerenciador1.set_senha("qualquer coisa")

print(gerenciador1.get_senha())

print(gerenciador1.is_correta("qualquer coisa"))