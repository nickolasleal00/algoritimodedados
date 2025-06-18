from PilhaDeLivros import PilhaDeLivros 
from ListaAutores import ListaAutores
from Autor import Autor
from Livro import Livro

def menu():
    lista_autores = ListaAutores()
    pilha_livros = PilhaDeLivros()

    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar autor")
        print("2 - Adicionar livro")
        print("3 - Remover livro")
        print("4 - Mostrar autores")
        print("5 - Mostrar pilha de livros")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do autor: ").strip()
            nacionalidade = input("Nacionalidade do autor: ").strip()
            autor = Autor(nome, nacionalidade)
            lista_autores.inserir_no_final(autor)

        elif escolha == "2":
            if lista_autores.topo is None:
                print("Nenhum autor cadastrado. Cadastre um autor antes.")
                continue
            titulo = input("Título do livro: ").strip()
            paginas = input("Número de páginas: ").strip()
            if not paginas.isdigit():
                print("Número de páginas inválido.")
                continue
            paginas = int(paginas)            
            print("Autores cadastrados:")
            atual = lista_autores.topo
            autores_disponiveis = []
            while atual:
                autores_disponiveis.append(atual.dado)
                print(f"{len(autores_disponiveis)} - {atual.dado.nome} ({atual.dado.nacionalidade})")
                atual = atual.prox
            escolha_autor = input("Escolha o número do autor do livro: ").strip()
            if not escolha_autor.isdigit() or int(escolha_autor) < 1 or int(escolha_autor) > len(autores_disponiveis):
                print("Opção de autor inválida.")
                continue
            autor_escolhido = autores_disponiveis[int(escolha_autor) - 1]
            livro = Livro(titulo, autor_escolhido, paginas)
            pilha_livros.addNoTopo(livro)

        elif escolha == "3":
            pilha_livros.removerDoTopo()

        elif escolha == "4":
            lista_autores.mostrar()

        elif escolha == "5":
            pilha_livros.mostrar()

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
