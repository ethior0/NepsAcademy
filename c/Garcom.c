#include <stdio.h>

int main() {

    int N, soma = 0, cc = 0;
    scanf("%d", &N);

    while(cc < N) {
        int L = 0, C = 0;
        scanf("%d%d", &L, &C);

        if (L > C) soma += C;
        cc++;
    }
    printf("%d", soma);
}
