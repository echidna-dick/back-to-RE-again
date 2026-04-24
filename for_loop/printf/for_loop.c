#include <stdio.h>

int main(){
    int x = 0;
    for(int i = 0; i < 10; i++){
        x++;
    }

    printf("x = %i <- (should be 10)", x);
    return 0;
}