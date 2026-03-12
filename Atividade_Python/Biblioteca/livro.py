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

            # Cria um objeto da classe Livro
            livro = Livro(titulo, autor, ano)

            # Adiciona o livro na biblioteca
            biblioteca.adicionar_livro(livro)

            print("Livro cadastrado com sucesso!")



        elif opcao == "2":

            # Solicita os dados do livro digital
            titulo = input("Título do livro digital: ")
            autor = input("Autor do livro digital: ")
            ano = int(input("Ano do livro digital: "))
            tamanho_arquivo = float(input("Tamanho do arquivo (MB): "))

            # Cria um objeto da classe LivroDigital (herança de Livro)
            livro = LivroDigital(titulo, autor, ano, tamanho_arquivo)

            # Adiciona o livro na biblioteca
            biblioteca.adicionar_livro(livro)

            print("Livro digital cadastrado com sucesso!")


        
        elif opcao == "3":

            # Solicita os dados do usuário
            nome = input("Nome do usuário: ")
            matricula = input("Matrícula do usuário: ")

            # Cria um objeto da classe Usuario
            usuario = Usuario(nome, matricula)

            # Adiciona o usuário à biblioteca
            biblioteca.cadastrar_usuario(usuario)

            print("Usuário cadastrado com sucesso!")



        elif opcao == "4":

            # Busca o usuário pela matrícula
            matricula = input("Digite a matrícula do usuário: ")
            usuario = biblioteca.buscar_usuario_por_matricula(matricula)

            # Se o usuário não existir
            if usuario is None:
                print("Usuário não encontrado.")
                continue

            # Busca o livro pelo título
            titulo = input("Digite o título do livro: ")
            livro = biblioteca.buscar_livro_por_titulo(titulo)

            # Verifica se o livro existe
            if livro is None:
                print("Livro não encontrado.")

            # Tenta realizar o empréstimo
            elif usuario.pegar_emprestado(livro):
                print("Empréstimo realizado com sucesso!")

            # Caso o livro já esteja emprestado
            else:
                print("Livro já está emprestado.")



        elif opcao == "5":

            # Busca o usuário
            matricula = input("Digite a matrícula do usuário: ")
            usuario = biblioteca.buscar_usuario_por_matricula(matricula)

            if usuario is None:
                print("Usuário não encontrado.")
                continue

            # Busca o livro a ser devolvido
            titulo = input("Digite o título do livro a devolver: ")
            livro = biblioteca.buscar_livro_por_titulo(titulo)

            if livro is None:
                print("Livro não encontrado.")

            # Tenta devolver o livro
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