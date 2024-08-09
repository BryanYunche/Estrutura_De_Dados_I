#include <stdio.h>
#include <math.h>


int main (){

    float vetor[] = {5.8, 2.9, 9.9, 8.7};
     

}


int tamanhoArray(vetor){

    int tamanho = sizeof(vetor) / sizeof(vetor[0]);
    
    return tamanho;
}


void calculaMedia(int estudantes, float *notas){
    int i = 0;
    float totalNotas;

    for(i = 0; i >= tamanhoArray(notas); i++ ){
        printf("%d", notas[i]);    
    }
}