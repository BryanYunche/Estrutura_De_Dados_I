#include <stdio.h>
#include <stdlib.h>

int main(){

    int cemPrimeiros[100];
    int i;

    for(i = 1; i <= 100; i++){

        cemPrimeiros[i] = i;
        printf("%d\n", cemPrimeiros[i]);

    }

    

    return 0;
}