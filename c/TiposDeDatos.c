@ -0,0 +1,19 @@
#include <stdio.h>

int main() {
    // Declaración de diferentes tipos de datos
    int entero = 10;
    float flotante = 3.14;
    double doble = 3.14159265359;
    char caracter = 'A';
    char cadena[] = "Hola, mundo";

    // Impresión de los valores de las variables
    printf("Entero: %d\n", entero);
    printf("Flotante: %f\n", flotante);
    printf("Doble: %lf\n", doble);
    printf("Caracter: %c\n", caracter);
    printf("Cadena: %s\n", cadena);

    return 0;
}