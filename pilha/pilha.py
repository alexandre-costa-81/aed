class No:
  def __init__(self, info=None, link=None):
    self.info = info
    self.link = link

class Pilha:
    def __init__(self):
        self.tamanho = 0
        self.topo = None
    
    def isEmpty(self):
        return (self.tamanho==0)
    
    def push(self, info):
        no = No(info)
        no.link = self.topo
        self.topo = no
        self.tamanho = self.tamanho + 1
    
    def pop(self):
        if (self.tamanho==0):
            return None
        else:
            removido = self.topo
            self.topo = removido.link
            self.tamanho = self.tamanho - 1
            return removido.info

# Funcao principal
def main():
    pilha = Pilha()

    pilha.push(10)
    pilha.push(20)

    while (pilha.isEmpty()==False):
        print pilha.pop()
     
    return

if __name__ == "__main__":
    main()