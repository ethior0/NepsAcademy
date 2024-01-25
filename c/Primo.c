#include <stdio.h>

int main() {

    int x, cc = 1, ccP = 1;
    scanf("%d", &x);

    while (cc < x/2) {
        if (x % cc == 0) ccP++;
        cc++;
    }
    printf(ccP == 2 ? "S" : "N");
}
