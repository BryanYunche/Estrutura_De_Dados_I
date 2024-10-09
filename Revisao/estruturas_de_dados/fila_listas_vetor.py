#Implementação de Filas por meio de vetores

#Em C geralmente definimos o tamanho do Vetor, todavia, em python podemos desconsiderar o fim de uma lista
#visto que o tamanho da lista é feita dinamicamente e variaveis não utilizadas são tratadas pelo garbage colector
class fila_lista():
    def __init__(self):
        self.fila_inicio = []

    def fila_vazia(self):
        if self.fila_inicio == []:
            return True
        else:
            return False

    def insere(self, valor):
        self.fila_inicio.append(valor)

    def remove(self):
        if self.fila_vazia:
            self.fila_inicio.pop(0)
        else:
            print('Fila vazia!')
    
    def imprime(self):
        print(20*'=')
        for valor in self.fila_inicio:
            print(f'{valor} ', end='')
    
        print()
    #Perceba que diferente da linguagem C eu não uso o Free para limpar os valores da memoria que a minha fila está alocada
    #pois o python tem o sistema de garbage colector para fazer isso
    def libera_lista(self):
        self.fila_inicio = []
    
        
    

