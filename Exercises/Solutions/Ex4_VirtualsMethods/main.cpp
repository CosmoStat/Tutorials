#include <iostream>
#include "rectangle.h"
#include "cercle.h"

using namespace std;

void affichage(const Figure *f){
    f->afficher_info();
    cout<<"Perimetre="<<f->perimetre()<<", Aire="<<f->surface()<<endl;
}

int main()
{
    Rectangle r=Rectangle(Point(1,2), Point(3,4));
    Cercle c=Cercle(Point(5,6), 7);
    Figure *f=&r;
    affichage(f);
    f=&c;
    affichage(f);
    return 0;
}
