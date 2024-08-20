#include <stdio.h>
#include <stdlib.h>
//Ler as notas obtidas por 5 alunos, calcular a média entre as notas lidas e apresentá-la. 

int main()
{
    float nota01, nota02, nota03, media;

    printf("Nota 01: ");
    scanf("%f", &nota01);

    printf("Nota 02: ");
    scanf("%f", &nota02);

    printf("Nota 03: ");
    scanf("%f", &nota03);

    media = ((nota01+nota02+nota03)/3);
    printf("Media: %4.2f", media);

    return 0;
}
