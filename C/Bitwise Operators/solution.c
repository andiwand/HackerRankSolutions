#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  int a = 0;
  int o = 0;
  int x = 0;
      
  for (int i = 1; i <= n; ++i) {
    for (int j = i + 1; j <= n; ++j) {
      int aa = i&j;
      int oo = i|j;
      int xx = i^j;
      if (aa > a && aa < k) {
        a = aa;
      }
      if (oo > o && oo < k) {
        o = oo;
      }
      if (xx > x && xx < k) {
        x = xx;
      }
    }
  }
  
  printf("%d\n", a);
  printf("%d\n", o);
  printf("%d\n", x);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
