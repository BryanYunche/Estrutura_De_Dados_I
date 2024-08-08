#include <stdio.h>

int main(){

    int cemPrimeiros[99];

    for (int i = 0; i < 99; i++){
        cemPrimeiros[i] = i;
    }

    printf("%d", cemPrimeiros);
    return 0;
}