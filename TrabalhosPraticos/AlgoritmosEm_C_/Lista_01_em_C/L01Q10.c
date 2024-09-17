#include <stdio.h>

//Ler um valor inteiro e apresentar seu antecessor e o seu sucessor

int main(){

    int valor;

    printf("Digite um valor: ");
    scanf("%d", &valor);

    printf("Antessessor: %d", valor-1);
    printf("\nValor dado: %d", valor);
    printf("\nSucessor: %d", valor+1);

    return 0;
}