#include <stdio.h>

int main() {

    int N, fat = 1;
    scanf("%d", &N);

    for (int i = N; i > 1; i--) {
        fat *= i;
    }

    printf("%d", fat);
}
