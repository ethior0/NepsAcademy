#include <stdio.h>

int main() {

    int A, B;
    scanf("%d%d", &A, &B);

    if ((A+B) % 2 == 0) {
        printf("Bino");
    } else {
        printf("Cino");
    }
}
