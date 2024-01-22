#include <stdio.h>

int main() {

    int D, p;
    scanf("%d", &D);

    if (D <= 800) p = 1;
    else if (D <= 1400) p = 2;
    else if (D <= 2000) p = 3;

    printf("%d", p);
}
