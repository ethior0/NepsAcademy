#include <stdio.h>

int main() {

    int N, cor = 0;
    scanf("%d", &N);

    int fita[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &fita[i]);
    }

    for (int j = 0; j < N; j++) {

        for (int k = 0; k < N; k++) {

            if (fita[k] == cor) {
                if (fita[k-1] == -1) {
                    if (cor + 1 > 9) fita[k-1] = cor;
                    else fita[k-1] = cor + 1;
                }
                if (fita[k+1] == -1) {
                    if (cor + 1 > 9)fita[k+1] = cor;
                    else fita[k+1] = cor+1;
                }
            }
        }
        if (cor < 9) {
            cor++;
        }
    }

    for (int m = 0; m < N; m++) {
        printf("%d ", fita[m]);
    }
}
