#include "point.h"

Point::Point(){
    x=0.;
    y=0.;
}

Point::Point(float x, float y){
    this->x=x;
    this->y=y;
}

Point::Point(const Point& rhs){
    this->x=rhs.x;
    this->y=rhs.y;
}

const Point& Point::operator=(const Point& rhs){
    x=rhs.x;
    y=rhs.y;
    return *this;
}

Point::~Point(){
}

float Point::getX()const{
    return x;
}

float Point::getY()const{
    return y;
}
