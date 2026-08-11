class Livro:

    def __init__(self, codigo, nome, autor):
        self.codigo= codigo
        self.nome= nome
        self.autor= autor
        self.emprestado = False
        

    def __str__(self):
         return f"Livro: {self.nome} do autor: {self.autor}"

    def __repr__(self):
        return self.__str__()

    