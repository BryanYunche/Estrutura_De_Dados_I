#include <stdio.h>

//Ler um valor inteiro e apresentá-lo acrescido de 25%.

int main(){
    int valor;

    printf("Digite um valor: ");
    scanf("%d", &valor);

    printf("\nValor mais 25 por cento: %.2f", valor+(valor*0.25));

    return 0;
}