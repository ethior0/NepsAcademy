#include <stdio.h>

int main() {

    int vetor[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &vetor[i]);
    }

    for (int j = 9; j >= 0; j--) {
        printf("%d\n", vetor[j]);
    }
}
