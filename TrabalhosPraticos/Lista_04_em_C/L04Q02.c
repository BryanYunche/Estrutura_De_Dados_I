#include <stdio.h>
#include <stdlib.h>

//Implemente um programa em C que calcula a média de um conjunto de 20 valores lidos de um vetor, sendo esses valores reais.  

double somaVetorDouble(double *vetor, int tamanhoVetor);

int main(){

    double valores[20] = {46.2, 81.2, 86.1, 64.5, 32.6, 86.9, 42.9, 19.3, 84.8, 90.5,
                      93.2, 76.2, 60.5, 88.9, 38.2, 24.5, 8.3, 92.0, 44.8, 8.5};

    int tamanho = sizeof(valores)/sizeof(valores[0]);

    double somaTotalMedia = somaVetorDouble(valores, tamanho);

    printf("Media de 20 valores: %.2f", somaTotalMedia/tamanho);
    

}

    
double somaVetorDouble(double *vetor, int tamanhoVetor){
    int i;
    double somaTotalVetorDouble = 0;

    for (i = 0; i < tamanhoVetor; i++){
        somaTotalVetorDouble += vetor[i];
    }

    return somaTotalVetorDouble;
}