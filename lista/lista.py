#!/usr/bin/env python
__author__      = "Alexandre Costa"
__copyright__   = "Copyright 2014, Projeto AED"
__credits__     = ["Alexandre Costa"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Alexandre Costa"
__email__       = "alexandre.costa@inf.ufpel.edu.br"
__status__      = "Desenvolvimento"

class No:
  def __init__(self, info=None, link=None):
    self.info = info
    self.link = link

class Lista:
    def __init__(self):
        self.tamanho = 0
        self.frente = None

    def insereInicioLista(self, info):
        no = No(info)
        no.link = self.frente
        self.frente = no

    def insereFimLista(self, info):
        no = No(info)
        ultimo = self.frente

        while (ultimo.link!=None):
            ultimo = ultimo.link

        ultimo.link = no

# Funcao principal
def main():
    lista = Lista()

    lista.insereInicioLista(10)
    lista.insereInicioLista(9)
    lista.insereFimLista(20)
    lista.insereInicioLista(30)
    
    imprime = lista.frente

    while (imprime!=None):
        print imprime.info
        imprime = imprime.link

    return

if __name__ == "__main__":
    main()
