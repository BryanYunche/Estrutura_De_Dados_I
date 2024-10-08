#Implementa os nós da lista encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo_node = None

#Implementação de lista encadeada
class Lista_encadeada:
    def __init__(self):
        #inicia a lista encadeada
        self.cabeca = None
    
    def adiciona_valor(self, dados):
        #cria o novo nó que será adicionado
        novo_no = Node(dados)

        #verifica se é uma lista encadeada vazia
        if self.cabeca == None:
            self.cabeca = novo_no
        else:
            #registra temporariamente os nós que passa
            ultimo_node_visitado = self.cabeca

            #Percorre a minha lista
            while ultimo_node_visitado.proximo_node != None:
                ultimo_node_visitado = ultimo_node_visitado.proximo_node
    
            #Quando encontra o ultimo node ele insere o nó
            ultimo_node_visitado.proximo_node = novo_no     

    def imprime_lista(self):

        if self.cabeca != None:            
            ultimo_node = self.cabeca

            while ultimo_node != None:
                    print(f'-> {ultimo_node.valor} ', end ='')
                    ultimo_node = ultimo_node.proximo_node

        else:
            print("Lita vazia!")


