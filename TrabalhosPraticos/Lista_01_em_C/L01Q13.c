#include <stdio.h>

//Ler a razão de uma PG(progressão geométrica) e o valor do 1º termo, em seguida calcular e apresentar o  5º termo da série.

int prineirpTermo, termoDesejado, razao;
double valorTermo; 

int main(){
    
    printf("Digite o primeiro termo da PA: ");
    scanf("%d", &prineirpTermo);

    printf("Digite a Razao da PA: ");
    scanf("%d", &razao);
    
    printf("Digite qual termo deseja encontrar: ");
    scanf("%d", &termoDesejado);

    valorTermo = prineirpTermo + ((termoDesejado - 1)*razao);

    printf("O valor do termo %d: %.2f", termoDesejado, valorTermo);
    
    return 0;
}