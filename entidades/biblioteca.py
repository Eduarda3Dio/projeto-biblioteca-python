from datetime import datetime, timedelta
from utilitarios.exceptions import UsuarioNaoCadastradoError
from utilitarios.exceptions import LivroNaoCadastradoError
from utilitarios.exceptions import LivroJaEmprestadoError
from utilitarios.exceptions import EmprestimoNaoEncontradoError
from entidades.emprestimo import Emprestimo

class Biblioteca:

    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_emprestimo(self, usuario, codigo):
        if usuario not in self.usuarios:
            raise UsuarioNaoCadastradoError("Usuário não cadastrado.")

        livro = self.buscar_livro(codigo)
             
        if livro is None:
            raise LivroNaoCadastradoError("Livro não cadastrado.")

        elif livro.emprestado:
            raise LivroJaEmprestadoError("Livro já emprestado.")

        else:
            livro.emprestado = True
            usuario.emprestar_livro(livro)
            data_emprestimo = datetime.now()
            data_devolucao_prevista = data_emprestimo + timedelta(days=15)

            emprestimo = Emprestimo(usuario, livro, data_emprestimo, data_devolucao_prevista)
            self.emprestimos.append(emprestimo)

    def buscar_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro

    def devolver_livro(self, codigo):
        encontrado = False

        for emprestimo in self.emprestimos:
            if emprestimo.livro.codigo == codigo and not emprestimo.devolvido:
                encontrado = True
                emprestimo.livro.emprestado = False
                emprestimo.usuario.livros_emprestados.remove(emprestimo.livro)
                emprestimo.devolvido = True

        if not encontrado:
            raise EmprestimoNaoEncontradoError("Empréstimo não encontrado.")


    def buscar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario

    def listar_livros(self):
        for livro in self.livros:
            print(livro)

    def listar_emprestimos(self):
        for emprestimo in self.emprestimos:
            print(emprestimo)


    