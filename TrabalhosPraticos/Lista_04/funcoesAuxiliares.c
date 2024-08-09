#include <stdio.h>
#include <stdlib.h>


int somaVetorInt(int *vetor, int tamanhoVetor){
    int i, somaTotalVetorInt = 0;

    for (i = 0; i < tamanhoVetor; i++){
        somaTotalVetorInt += vetor[i];
    }

    return somaTotalVetorInt;
}

int main(){

    int vetorrr[4] = {1, 2, 3, 4};

    int tamanhoVetor = sizeof(vetorrr)/sizeof(vetorrr[0]);

    printf("tamanho vetor: %d", somaVetorInt(vetorrr, tamanhoVetor));

    return 0;
}

