class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        return disponiveis

    def listar_livros_emprestados(self):
        emprestados = [livro for livro in self.livros if not livro.disponivel]
        return emprestados

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def buscar_usuario_por_matricula(self, matricula):
        for usuario in self.usuarios:
            if usuario.matricula == matricula:
                return usuario
        return None