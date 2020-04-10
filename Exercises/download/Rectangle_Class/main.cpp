#include <iostream>
#include "point.h"
#include "rectangle.h"

using namespace std;

int main()
{
    Point p1(1,2);
    Point p2(3,4);
    Rectangle a(p1,p2);
    a.afficher_info();
    a.deplacer(3,4);
    a.afficher_info();
    return 0;
}
