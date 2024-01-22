#include <stdio.h>

int main() {

    int vetor[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &vetor[i]);
    }

    int X;
    scanf("%d", &X);

    for (int i = 0; i < 10; i++) {
        if (*(vetor + i) == X) {
            printf("SIM");
            break;
        } else if (i == 9) {
            printf("NAO");
        }
    }

}
