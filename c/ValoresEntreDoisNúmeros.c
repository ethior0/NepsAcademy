#include <stdio.h>

// � preciso declarar as fun��es antes
// ou criar elas antes da fun�ao main, EX:
// int min(int par1, int par2);
// int max(int par1, int par2);

int min(int par1, int par2) {
    return par1 > par2 ? par2 : par1;
}

int max(int par1, int par2) {
    return par1 > par2 ? par1 : par2;
}

int main() {

    int A, B;
    scanf("%d%d", &A, &B);

    for (int i = min(A,B); i <= max(A,B); i++) {
        printf("%d ", i);
    }
}
