#include <stdio.h>
#include <math.h>

int main() {

    int N, cc = 0;
    scanf( "%d", &N );

    while( cc < N ) {
        float num;
        scanf( "%f", &num );
        printf( "%.4f\n", sqrt(num) );
        cc++;
    }
}
