class Emprestimo:
	
	def __init__(self, usuario, livro, data_emprestimo, data_devolucao_prevista):
		self.usuario= usuario
		self.livro= livro
		self.data_emprestimo= data_emprestimo
		self.data_devolucao_prevista= data_devolucao_prevista
		self.devolvido = False


	def __str__(self):
	    return (
	        "\n========== EMPRÉSTIMO ==========\n"
	        f"Usuário: {self.usuario.nome}\n"
	        f"Livro: {self.livro.nome}\n"
	        f"Data do empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y')}\n"
	        f"Devolução prevista: {self.data_devolucao_prevista.strftime('%d/%m/%Y')}\n"
	        f"Devolvido: {'Sim' if self.devolvido else 'Não'}\n"
	        "================================"
	    )