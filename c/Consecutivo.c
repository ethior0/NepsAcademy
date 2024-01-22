#include <stdio.h>

int main() {

    int N, aux, cc = 0, p = 1, max = 0;
    scanf("%d", &N);

    while (cc < N) {
        int num;
        scanf("%d", &num);

        if (cc == 0) {
            aux = num;
        } else {
            if (num == aux) {
                p++;
                if (p >= max) max = p;
            } else {
                aux = num;
                p = 1;
            }
        }
        cc++;
    }
    printf("%d", max);
}
