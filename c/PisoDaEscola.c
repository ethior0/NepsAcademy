#include <stdio.h>

int main() {

    int L, C, cc2 = 0, cc = 0;
    float a = 0;

    scanf("%d%d", &L, &C);
    a += (L - 1) * 0.25 * 2; // lajotas tipo 2 de direita e esquerda
    a += C  * 0.25 * 2; // lajotas tipo 2 de cima e baixo

    cc2 = ( a - (0.125 * 4) ) / 0.25;

    while(a < L*C) {
        cc++;
        a += 0.5;
    }

    printf("%d\n", cc);
    printf("%d", cc2);
}
