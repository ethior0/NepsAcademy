#include <stdio.h>

int main() {

    int X;
    scanf("%d", &X);

    for (int i = 1; i <= 10; i++) {
        printf("%d * %d = %d\n", X, i, X*i);
    }
}
