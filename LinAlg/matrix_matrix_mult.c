/**
 * Performs matrix - matrix multiplication
 * between A (MxK) and B (KxN)
 */
#include <stdio.h>

int main(int argc, char **argv){
    int A[3][3] = {
        {4, 0, 0},
        {0, 3, 0},
        {0, 0, 2}
    };
    int B[3][3] = {
        {3, -2, 4},
        {7, 4, 5},
        {3, 2, 1}
    };

    int C[3][3] = {0};

    int i, j, k;

    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            int sum = 0;
            for (k = 0; k < 3; k++){
                sum += A[i][k]*B[k][j];
            }
            C[i][j] = sum;
        }
    }

    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            printf("%2d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}


