#include <stdio.h>
#include <stdlib.h>
#include <math.h>


//Ler um número inteiro e apresentar: NUMERO=xx, QUADRADO=xx e RAIZ QUADRADA=xx

int main()
{

double numero, quadrado, raizquadrada;

printf("Digite um numero: ");
scanf("%lf", &numero);

printf("\nNumero digitado: %.2lf", numero);
printf("\nNumero elevado ao quadrado: %.2lf", pow(numero, 2));
printf("\nRaiz do numero: %.2lf", sqrt(numero));

}

