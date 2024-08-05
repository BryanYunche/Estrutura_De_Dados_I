#include <stdio.h>

//Ler um tempo em segundos e apresentá-lo convertido em Horas: Minutos: Segundos.

int main(){

    int segundos, horaInteira, minutoInteiro, segundosSobra;
    double minutos, horas, restoHora, restoMinuto;

    printf("Digite um valor em segundos: ");
    scanf("%d", &segundos);

    //Calcula o valor total em horas
    horas = segundos/3600 ; //Perceba que aqui tem o total em horas de todos os segundos digitados
    
    horaInteira = (int)horas;

    restoHora = horas - horaInteira;

    minutos = (restoHora*60);

    minutoInteiro = (int)minutos;

    restoMinuto = minutos - minutoInteiro;

    segundosSobra = restoMinuto * 60;

    printf("\nHoras: %d", horaInteira);
    printf("\nMinuto: %d", minutoInteiro);
    printf("\nSegundo: %d", segundosSobra);

    //Deixa no formato
    //printf("\nHoras: %d Minutos: %d Segundos: %d ", horas);


    return 0;
}