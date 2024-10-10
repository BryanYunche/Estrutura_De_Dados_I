#Listas: É uma estrutura de dados que armazena elementos em uma sequência. 
#Segue a ordem LIFO (Last In, First Out), o que significa que o último elemento a ser inserido é o primeiro a ser removido

#Pilhas usando Vetores--------------------------------------
from pilha_vetor import pilha_vetor

exemplo_pilha_vetor = pilha_vetor()

exemplo_pilha_vetor.adiciona('A')
exemplo_pilha_vetor.adiciona('B')
exemplo_pilha_vetor.adiciona('C')
exemplo_pilha_vetor.adiciona('D')
exemplo_pilha_vetor.adiciona('E')

exemplo_pilha_vetor.imprime_pilha()

exemplo_pilha_vetor.remove()
exemplo_pilha_vetor.remove()

exemplo_pilha_vetor.imprime_pilha()

#Pilhas usando lista_encadeada ----------------------------------
from pilha_encadeada import pilha_encadeada

print(20*'+-+')

exemplo_pilha_encadeada = pilha_encadeada()

exemplo_pilha_encadeada.insere('Primeiro')
exemplo_pilha_encadeada.insere('Segundo')
exemplo_pilha_encadeada.insere('Terceiro')
exemplo_pilha_encadeada.insere('Quarto')
exemplo_pilha_encadeada.insere('Quinto')

exemplo_pilha_encadeada.imprime()

exemplo_pilha_encadeada.remove()

exemplo_pilha_encadeada.imprime()

exemplo_pilha_encadeada.remove()
exemplo_pilha_encadeada.remove()
exemplo_pilha_encadeada.remove()

exemplo_pilha_encadeada.imprime()

exemplo_pilha_encadeada.remove()
exemplo_pilha_encadeada.remove()

