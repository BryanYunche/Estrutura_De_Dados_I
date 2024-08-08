#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Ler a base e a altura de um retângulo e apresentar: PERIMETRO=xx, AREA=xx e DIAGONAL=xx

//teste git

int main (){

    int base, altura;
    float perimetro, area, diagonal;
    

    printf("Digite o valor da Base: ");
    scanf("%d", &base);
    printf("Digite o valor da Altura: ");
    scanf("%d", &altura);

    //Calculo Perimetro
    perimetro = 2*(base+altura);
    area = base*altura;
    diagonal = sqrt(pow(base, 2) + pow(altura, 2));

    printf("Base: %d \nAltura: %d ", base, altura);
    printf("\n Perimetro: %.2f", perimetro);
    printf("\n Area: %.2f", area);
    printf("\n Diagonal: %.2f", diagonal);
    
    return 0;
}