#Implementar uma pilha a partir da estrutura de listas dinâmicas em python

class pilha_vetor():

    def __init__(self):
        self.valores = []

    def adiciona(self, valor):
        self.valores.append(valor)
    

    def remove(self):
        if len(self.valores) != 0:
            valor_retirado = self.valores.pop()
            print(f'Valor retirado: {valor_retirado}')
        else:
            print('Lista vazia!')
    
    def imprime_pilha(self):
        if len(self.valores) != 0:
          pilha = self.valores[::-1]
          for valor in pilha:
              print(f'| {valor} |')
