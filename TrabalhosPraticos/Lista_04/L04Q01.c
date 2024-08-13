#include <stdio.h>
#include <stdlib.h>

//Fazer um programa em C para calcular a soma dos 100 primeiros números inteiros usar vetores.

int somaVetorInt(int *vetor, int tamanhoVetor);

int main(){
    int i;
    int cemPrimeiros[100];
    int tamanho = sizeof(cemPrimeiros)/sizeof(cemPrimeiros[0]);

    for(i = 0; i < 100; i++){
        cemPrimeiros[i] = i+1;
    }

    printf("Soma dos 100 primeiros termos: %d", somaVetorInt(cemPrimeiros, tamanho));

    return 0;
}

int somaVetorInt(int *vetor, int tamanhoVetor){
    int i, somaTotalVetorInt = 0;

    for (i = 0; i < tamanhoVetor; i++){
        somaTotalVetorInt += vetor[i];
    }

    return somaTotalVetorInt;
}