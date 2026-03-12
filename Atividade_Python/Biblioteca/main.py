from livro import Livro, LivroDigital
from usuario import Usuario
from biblioteca import Biblioteca


def exibir_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro físico")
    print("2 - Cadastrar livro digital")
    print("3 - Cadastrar usuário")
    print("4 - Realizar empréstimo")
    print("5 - Devolver livro")
    print("6 - Listar livros disponíveis")
    print("7 - Listar livros emprestados")
    print("8 - Sair")


def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano do livro: "))
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
            print("Livro cadastrado com sucesso!")

        elif opcao == "2":
            titulo = input("Título do livro digital: ")
            autor = input("Autor do livro digital: ")
            ano = int(input("Ano do livro digital: "))
            tamanho_arquivo = float(input("Tamanho do arquivo (MB): "))
            livro = LivroDigital(titulo, autor, ano, tamanho_arquivo)
            biblioteca.adicionar_livro(livro)
            print("Livro digital cadastrado com sucesso!")

        elif opcao == "3":
            nome = input("Nome do usuário: ")
            matricula = input("Matrícula do usuário: ")
            usuario = Usuario(nome, matricula)
            biblioteca.cadastrar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "4":
            matricula = input("Digite a matrícula do usuário: ")
            usuario = biblioteca.buscar_usuario_por_matricula(matricula)

            if usuario is None:
                print("Usuário não encontrado.")
                continue

            titulo = input("Digite o título do livro: ")
            livro = biblioteca.buscar_livro_por_titulo(titulo)

            if livro is None:
                print("Livro não encontrado.")
            elif usuario.pegar_emprestado(livro):
                print("Empréstimo realizado com sucesso!")
            else:
                print("Livro já está emprestado.")

        elif opcao == "5":
            matricula = input("Digite a matrícula do usuário: ")
            usuario = biblioteca.buscar_usuario_por_matricula(matricula)

            if usuario is None:
                print("Usuário não encontrado.")
                continue

            titulo = input("Digite o título do livro a devolver: ")
            livro = biblioteca.buscar_livro_por_titulo(titulo)

            if livro is None:
                print("Livro não encontr1ado.")
            elif usuario.devolver_livro(livro):
                print("Livro devolvido com sucesso!")
            else:
                print("Este usuário não está com esse livro.")

        elif opcao == "6":
            livros = biblioteca.listar_livros_disponiveis()
            if livros:
                print("\n--- LIVROS DISPONÍVEIS ---")
                for livro in livros:
                    print(livro)
            else:
                print("Não há livros disponíveis.")

        elif opcao == "7":
            livros = biblioteca.listar_livros_emprestados()
            if livros:
                print("\n--- LIVROS EMPRESTADOS ---")
                for livro in livros:
                    print(livro)
            else:
                print("Não há livros emprestados.")

        elif opcao == "8":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()