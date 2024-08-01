#include <stdio.h>
#include <math.h>

int main (){
    float a = 15.8;

    float b = a - floor(a);

    printf("%f", b);
    return 0;
}