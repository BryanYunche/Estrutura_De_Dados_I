#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    //Vari�veis onde vai ser armazenado os valores
    int num01, num02;

    //Vari�veis de Soma, Diferen�a, Produto, M�dia.
    int SOMA, DIFERENCA, PRODUTO, MEDIA;

    //Ler dois valores inteiros e apresentar sua: SOMA=xx, DIFEREN�A=xx, PRODUTO=xx, e M�DIA=xx
    printf("Digite um numero inteiro:");
    scanf("%d", &num01);
    printf("\nDigite outro numero inteiro:");
    scanf("%d", &num02);

    //Calcula a soma
    SOMA =  num01 + num02;
    DIFERENCA = num01 - num02;
    PRODUTO = num01*num02;
    MEDIA = (num01+num02)/2;

    printf("\nSoma: %d\nDiferenca: %d\nProduto: %d\nMedia: %d", SOMA, DIFERENCA, PRODUTO, MEDIA);

    return 0;
}
