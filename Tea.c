#include <stdio.h>
 
int main() {
 
    int count = 0;
    int T;
    int A, B, C, D, E; 
    scanf("%i", &T);
    scanf("%i %i %i %i %i", &A,&B,&C,&D,&E);
    
    if(T == A) count++;
    if(T == B) count++;
    if(T == C) count++;
    if(T == D) count++;
    if(T == E) count++;
    printf("\n%i", count);
    return 0;
}