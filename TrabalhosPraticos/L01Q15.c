#include <stdio.h>

//Ler um tempo em segundos e apresentá-lo convertido em Horas: Minutos: Segundos.

int main(){

    int segundos, horaInteira, minutoInteiro;
    double minutos, horas, restoHora, restoMinuto;

    printf("Digite um valor em segundos: ");
    scanf("%d", segundos);

    //Calcula o valor total em horas
    minutos = segundos/60;
    horas = minutos/60;
    
    //Partes Inteiras
    horaInteira = (int)horas;

    //Calculando resto de horas
    restoHora = horas - horaInteira;

    minutoInteiro = (int)minutos + (restoHora*60);

    printf("Horas: ")




    //Deixa no formato
    printf("\nHoras: %d Minutos: %d Segundos: %d ", horas);


    return 0;
}