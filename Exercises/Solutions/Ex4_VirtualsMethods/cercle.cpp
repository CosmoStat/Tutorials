#include <math.h>
#include <iostream>
#include "cercle.h"

using namespace std;

Cercle::Cercle(){
    rayon=0;
}


Cercle::Cercle(const Cercle& rhs){
    centre=rhs.centre;
    rayon=rhs.rayon;
}

const Cercle& Cercle::operator=(const Cercle& rhs){
    centre=rhs.centre;
    rayon=rhs.rayon;
    return *this;
}

Cercle::~Cercle(){
}


Cercle::Cercle(Point centre, float rayon){
    this->centre=centre;
    this->rayon=rayon;
}

void Cercle::afficher_info()const{
    cout<<"Cercle de rayon "<<rayon<<" et de centre ("<<centre.getX()<<", "<<centre.getY()<<")"<<endl;
}


float Cercle::perimetre()const{
    return M_PI*rayon;
}

float Cercle::surface()const{
    return M_PI*rayon*rayon;
}
