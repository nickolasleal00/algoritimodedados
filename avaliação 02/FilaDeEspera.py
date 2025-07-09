from No import No
from Apartamento import Apartamento

class FilaDeEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.prox = None

    def adicionar(self, apartamento = Apartamento):
        nodo = No(apartamento)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.imprimir()
    
    def imprimir(self):
        print("-------- Fila De Espera -----------------------")
        if self.inicio is None:
            print( "Fila está vazia!" )
        else:
            aux = self.inicio
            txt = ""
            while aux :
                txt += aux.dado  + " - "
                aux = aux.prox
            print( txt )
    
    def remover(self):
        if self.inicio is not None:
            elemento = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            print( "O apartamento número ", elemento.dado, "foi removido" )
        self.imprimir()