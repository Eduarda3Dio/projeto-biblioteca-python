from entidades.biblioteca import Biblioteca
from entidades.livros import Livro
from entidades.usuario import Usuario
from utilitarios.exceptions import (UsuarioNaoCadastradoError,LivroNaoCadastradoError,LivroJaEmprestadoError)

biblioteca = Biblioteca()

while True:
    print("\n========== BIBLIOTECA ==========")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Listar livros")
    print("6 - Consultar empréstimos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Digite o código do livro: "))
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")

        livro = Livro(codigo, nome, autor)
        biblioteca.cadastrar_livro(livro)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do usuario: ")
        cpf = input("Digite o cpf do usuario: ")

        usuario = Usuario(nome, cpf)
        biblioteca.cadastrar_usuario(usuario)
        print("Usuario cadastrado com sucesso!")

    elif opcao == "3":
        cpf = input("Digite o CPF do usuario: ")
        codigo = int(input("Digite o código do livro: "))

        try:
            usuario = biblioteca.buscar_usuario(cpf)
            biblioteca.realizar_emprestimo(usuario, codigo)

            print("Empréstimo realizado com sucesso!")

        except UsuarioNaoCadastradoError:
            print("Usuário não cadastrado.")

        except LivroNaoCadastradoError:
            print("Livro não cadastrado.")

        except LivroJaEmprestadoError:
            print("Livro já está emprestado.")


    elif opcao == "4":
        codigo = int(input("Digite o código do livro: "))

        try:
            biblioteca.devolver_livro(codigo)
            print("Livro devolvido com sucesso!")

        except EmprestimoNaoEncontradoError:
            print("Empréstimo não encontrado.")

    elif opcao == "5":
        biblioteca.listar_livros()

    elif opcao == "6":
        biblioteca.listar_emprestimos()

    elif opcao == "0":
        print("Sistema encerrado.")
        break
