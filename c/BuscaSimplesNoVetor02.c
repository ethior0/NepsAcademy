#include <stdio.h>

int main() {

    int vetor[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &vetor[i]);
    }

    int X, cc = 0;
    scanf("%d", &X);

    for (int j = 0; j < 10; j++) {
        if (*(vetor + j) == X) {
            cc++;
        } else if (j == 9 && cc == 0) {
            printf("Mia x");
        }
    }

    if (cc > 0) {
        printf("%d\n", cc);
        for (int k = 0; k < 10; k++) {
            if (*(vetor + k) == X) {
                printf("%d", k);
                if (k <= 8) {
                    printf(" ");
                }
            }
        }
    }

}
