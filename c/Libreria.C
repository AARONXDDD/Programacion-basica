@@ -0,0 +1,15 @@
#include <stdio.h>
#include <math.h>

int main() {
    double num, result;

    printf("Ingresa un número: ");
    scanf("%lf", &num);

    result = sqrt(num);

    printf("La raíz cuadrada de %.2lf es %.2lf\n", num, result);

    return 0;
}