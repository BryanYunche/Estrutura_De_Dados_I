#Listas: É uma estrutura de dados que armazena elementos em uma sequência. 
#Segue a ordem LIFO (Last In, First Out), o que significa que o último elemento a ser inserido é o primeiro a ser removido

#Pilhas usando Vetores--------------------------------------
from pilha import pilha_vetor

exemplo_pilha_vetor = pilha_vetor()

exemplo_pilha_vetor.adiciona('A')
exemplo_pilha_vetor.adiciona('B')
exemplo_pilha_vetor.adiciona('C')
exemplo_pilha_vetor.adiciona('D')
exemplo_pilha_vetor.adiciona('E')

exemplo_pilha_vetor.imprime_pilha()
