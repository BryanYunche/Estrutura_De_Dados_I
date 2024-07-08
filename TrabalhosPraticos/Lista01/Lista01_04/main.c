#include <stdio.h>
#include <stdlib.h>

int main()
{
    float valor01, valor02, valor03, valor04;

    printf("Valor 01: ");
    scanf("%f", &valor01);

    printf("Valor 02: ");
    scanf("%f", &valor02);

    printf("Valor 03: ");
    scanf("%f", &valor03);

    printf("Valor 04: ");
    scanf("%f", &valor04);


    printf("Valor: %4.2f %4.2f %4.2f %4.2f", &valor01, &valor02, &valor03, &valor04);
    return 0;
}
