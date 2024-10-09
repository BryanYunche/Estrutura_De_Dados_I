#Implementa os nós da lista encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo_node = None

#Implementação de lista encadeada
class fila_Lista_encadeada:
    def __init__(self):
        #inicia a lista encadeada
        self.inicio = None
        self.fim = None
    
    def adiciona_valor(self, dados):
        #cria o novo nó que será adicionado
        novo_no = Node(dados)

        #verifica se é uma lista encadeada vazia
        if self.fim:
            self.fim.proximo_node = novo_no
        self.fim = novo_no

        if self.inicio is None:
            self.inicio = novo_no

    def remove(self):
        if self.inicio == None:
            print("Fila vazia!")
        elif self.inicio:
            print(f'Valor removido: {self.inicio.valor}')
            
            #Tira o nó e muda a posição do inicio da fila
            self.inicio = self.inicio.proximo_node

            #Verifica se ao tirar o nó a lista fica vazia
            if self.inicio == None:
                self.fim = None

    def imprime_lista(self):
        print(20*'-')
        if self.inicio != None:            
            ultimo_node = self.inicio

            while ultimo_node != None:
                    print(f' -> {ultimo_node.valor}', end ='')
                    ultimo_node = ultimo_node.proximo_node
        else:
            print("Lita vazia!")

        print()
        print(20*'-')