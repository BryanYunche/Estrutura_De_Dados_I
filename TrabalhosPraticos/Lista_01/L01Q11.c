#include <stdio.h>

//Ler a notas da PR1 e PR2  e apresentar: MÉDIA REAL=xx, MÉDIA TRUNCADA=xx

int main(){
    
    double pr1, pr2, mediaReal, mediaTruncada;

    printf("Digite o valor da prova 01: ");
    scanf("%lf", &pr1);

    printf("\nDigite o valor da prova 02: ");
    scanf("%lf", &pr2);

    mediaReal = ((pr1+pr2)/2);
    mediaTruncada = mediaReal;

    printf("\nMedia Real: %.2f\nMedia Truncada: %.2f", mediaReal, mediaTruncada);

    return 0;
}