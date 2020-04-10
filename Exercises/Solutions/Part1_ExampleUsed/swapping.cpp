#include <iostream>

using namespace std;

int main()

{

 int i = 2, j = 5, t;

 cout << " i = " << i << ", j = " << j << endl;

 t = i;

 i = j;

 j = t;

 cout << " i = " << i << ", j = " << j << endl;

 return 0;

}