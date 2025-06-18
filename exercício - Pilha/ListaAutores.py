from Autor import Autor
from No import No

class ListaAutores:
    def __init__(self):
        self.topo = None

    def inserir_no_final(self, autor: Autor):
        novo_no = No(autor)
        if self.topo is None:
            self.topo = novo_no
            print(f"Autor '{autor.nome}' adicionado como primeiro da lista.")
        else:
            atual = self.topo
            while atual.prox:
                atual = atual.prox
            atual.prox = novo_no
            print(f"Autor '{autor.nome}' adicionado no final da lista.")

    def mostrar(self):
        atual = self.topo
        if atual is None:
            print("Lista de autores vazia.")
            return
        print("Lista de Autores:")
        while atual:
            autor = atual.dado
            print(f"  - {autor.nome} ({autor.nacionalidade})")
            atual = atual.prox
