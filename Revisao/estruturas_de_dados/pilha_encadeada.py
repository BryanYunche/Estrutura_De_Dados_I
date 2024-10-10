#Implementar pilha a partir de fila encadeada

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo_no = None

class pilha_encadeada:

    def __init__(self):
        self.pilha_topo = None

    def insere(self, item):

        novo_no = Node(item)

        #Caso o topo da pilha não esteja vazia
        if self.pilha_topo:
            novo_no.proximo_no = self.pilha_topo
            self.pilha_topo = novo_no         
        else:
            self.pilha_topo = novo_no   

    def remove(self):
        
        #Verifica se a pilha está vazia
        if self.pilha_topo:
            print(f'Valor retirado: {self.pilha_topo.valor}')
            self.pilha_topo = self.pilha_topo.proximo_no
        else:
            print(f'Tem nada mais pra tirar aqui meu cria.')


    def imprime(self):
        
        if self.pilha_topo:
            #Enquanto a fila não for vazia
            iterador = self.pilha_topo
            while iterador:
                print(f'| {iterador.valor} |')
                iterador = iterador.proximo_no
        else:    
            print('A fila está vazia!')

    def libera(self):
        self.pilha_topo = None


