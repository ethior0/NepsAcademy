#include <stdio.h>

int main() {

    int N, cc = 0, a = 0, b = 1, c = 1;
    scanf("%d", &N);

    while (cc < N) {
        c = a + b;
        a = b;
        b = c;
        cc++;
    }

    printf("%d", c);
}
