#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Criar 3 variáveis (espaços de memória) de nome M1, M2 e M3, para armazenar valores inteiros;
    int M1, M2, M3;

    //Armazenar a constante 10 na posição de memória M3;
    M3 = 10;

    //Ler um valor inteiro colocando-o na posição de memória M1;
    printf("Adicione um numero inteiro: ");
    scanf("%d", &M1);

    //Armazenar na posição de memória M2 o conteúdo da posição de memória M1 mais 8 unidades;
    M2 = M1 + 8;

    //Apresentar o conteúdo das posições de memória M1, M2 e M3, identificando-os;
    printf("\nM1: %d M2: %d M3: %d", M1, M2, M3);

    //Adicionar o conteúdo das posições de memória M1 e M2 a posição de memória M3;
    M3 = M1 + M2;

    //Armazenar na posição de memória M3 o triplo de sua metade;
    M3 = 3*(M3/2);

    //Adicionar uma unidade a posição de memória M3;
    M3 = M3 + 1;

    //Apresentar o conteúdo da posição de memória M3, identificando-o;
    printf("\nM3: %d", M3);

    return 0;
}
