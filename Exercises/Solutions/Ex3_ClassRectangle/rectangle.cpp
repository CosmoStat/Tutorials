#include "rectangle.h"
#include <iostream>

using namespace std;

Rectangle::Rectangle()
{
    //ctor
}

Rectangle::~Rectangle()
{
    //dtor
}

Rectangle::Rectangle(const Point& p1, const Point& p2){
    this->p1=p1;
    this->p2=p2;
}

Rectangle::Rectangle(const Rectangle& rhs){
    this->p1=rhs.p1;
    this->p2=rhs.p2;
}

const Rectangle& Rectangle::operator =(const Rectangle& rhs){
    this->p1=rhs.p1;
    this->p2=rhs.p2;
    return *this;
}

void Rectangle::afficher_info()const{
    cout<<"Rectangle avec les coins ("<<p1.getX()<<", "<<p1.getY()<<") et ("<<p2.getX()<<", "<<p2.getY()<<")"<<endl;
}

void Rectangle::deplacer(float dx, float dy){
    p1=Point(p1.getX()+dx, p1.getY()+dy);
}

