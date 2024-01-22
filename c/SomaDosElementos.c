#include <stdio.h>

int main() {

    int N, soma = 0;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);
        soma += num;
    }
    printf("%d", soma);
}
