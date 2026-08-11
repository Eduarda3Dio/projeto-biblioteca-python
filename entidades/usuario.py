class Usuario:

	def __init__(self, nome, cpf):
		self.nome= nome
		self.cpf= cpf
		self.livros_emprestados = [] #lista vazia para adicionar os emprestimos
		
	def emprestar_livro(self, livro):

		self.livros_emprestados.append(livro)