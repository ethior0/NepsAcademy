#include <stdio.h>

int main() {

    int X, cc = 1;
    scanf("%d", &X);

    while (cc <= X) {
        if (X % cc == 0 && cc < X) {
            printf("%d ", cc);
        }
        if (X % cc == 0 && cc == X) {
            printf("%d");
        }
        cc++;
    }
}
