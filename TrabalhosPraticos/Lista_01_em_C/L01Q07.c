#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Ler o raio de um  círculo e apresentar: PERÍMETRO=xx e ÁREA=xx

int main(){

    int raio;

    double perimetro, area;

    printf("Digite o raio: ");
    scanf("%d", &raio);


    area = 3.14*pow(raio, 2);

    perimetro = 2*3.14*raio;

    printf("\nRaio: %d", raio);
    printf("\nPerimetro: %.2f", perimetro);
    printf("\nArea: %.2f", area);

    return 0;

}