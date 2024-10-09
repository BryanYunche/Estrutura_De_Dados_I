#Listas: É uma estrutura de dados que armazena elementos em uma sequência. 
# Cada elemento tem uma posição específica, e é possível acessar diretamente os elementos pela sua posição.


#Fila usando Lista/vetores --------------------------------------------------------------------
from fila_listas_vetor import fila_lista

exemplo_fila_vetor = fila_lista()

exemplo_fila_vetor.insere(1)
exemplo_fila_vetor.insere(2)
exemplo_fila_vetor.insere(3)
exemplo_fila_vetor.insere(4)
exemplo_fila_vetor.insere(5)

exemplo_fila_vetor.imprime()

exemplo_fila_vetor.remove()
exemplo_fila_vetor.remove()
exemplo_fila_vetor.remove()

exemplo_fila_vetor.imprime()


#Fila usando Lista Encadeada ----------------------------------------------------------
from fila_lista_encadeada import fila_Lista_encadeada

exemplo_lista_encadeada = fila_Lista_encadeada()
exemplo_lista_encadeada.adiciona_valor(1)
exemplo_lista_encadeada.adiciona_valor(2)
exemplo_lista_encadeada.adiciona_valor(3)
exemplo_lista_encadeada.adiciona_valor(4)
exemplo_lista_encadeada.adiciona_valor(5)

exemplo_lista_encadeada.imprime_lista()

exemplo_lista_encadeada.remove()
exemplo_lista_encadeada.remove()

exemplo_lista_encadeada.imprime_lista()

exemplo_lista_encadeada.remove()
exemplo_lista_encadeada.remove()
exemplo_lista_encadeada.remove()

exemplo_lista_encadeada.imprime_lista()

exemplo_lista_encadeada.remove()



#Recursivas
#Circulares
