#include <stdio.h>
#include <stdlib.h>
//Ler quatro valores reais e apresentar a média ponderada, considerando os pesos 1, 2, 3 e 4, respectivamente.

int main()
{
    float valor01, valor02, valor03, valor04, mediaPonderada,pesos;

    printf("Valor 01: ");
    scanf("%f", &valor01);

    printf("Valor 02: ");
    scanf("%f", &valor02);

    printf("Valor 03: ");
    scanf("%f", &valor03);

    printf("Valor 04: ");
    scanf("%f", &valor04);


    printf("Valor: %4.2f %4.2f %4.2f %4.2f", valor01*1, valor02*2, valor03*3, valor04*4);

    pesos = 1+2+3+4;

    mediaPonderada = (((valor01*1) + (valor02*2) + (valor03*3) + (valor04*4))/pesos);

    printf("\nSua media ponderada e: %f", mediaPonderada);
    return 0;
}
