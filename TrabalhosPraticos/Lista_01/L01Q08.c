#include <stdio.h>
#include <math.h>

// Ler o valor de um lado do quadrado  e apresentar: PERÍMETRO=xx, ÁREA=xx e DIAGONAL=xx 

int main(){

    int ladoQuadrado;
    double area, perimetro, diagonal;

    printf("Escreva o lado do quadrado: ");
    scanf("%d", &ladoQuadrado);

    area = pow(ladoQuadrado, 2);
    perimetro = ladoQuadrado*4;
    diagonal = ladoQuadrado*sqrt(2);

    printf("\nLado do Quadrado: %.2f", ladoQuadrado);
    printf("\nArea: %.2f", area);
    printf("\nPerimetro: %.2f", perimetro);
    printf("\nDiagonal: %.2f", diagonal);

    return 0;
}