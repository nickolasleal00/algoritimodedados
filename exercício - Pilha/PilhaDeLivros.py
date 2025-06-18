from No import No
from Autor import Autor
from Livro import Livro

class PilhaDeLivros:
    def __init__(self):
        self.topo = None
        self.removido = None    
    
    def addNoTopo(self, livro: Livro):
        novo_no = No(livro)
        novo_no.prox = self.topo
        self.topo = novo_no
        print(f"Livro '{livro.titulo}' adicionado ao topo da pilha.")

    def removerDoTopo(self,):
       if self.topo is None:
          print("A lista está vazia")
       else:
            self.removido = self.topo.dado
            print(f"Removido do topo: '{self.removido.titulo}' por {self.removido.autor.nome}")
            self.topo = self.topo.prox   
    
    def mostrar(self,):
        atual = self.topo
        if atual is None:
            print("Pilha de livros vazia.")
            return
        print("Pilha de Livros:")
        while atual:
            livro = atual.dado
            print(f"  - '{livro.titulo}' de {livro.autor.nome} ({livro.paginas} páginas)")
            atual = atual.prox

