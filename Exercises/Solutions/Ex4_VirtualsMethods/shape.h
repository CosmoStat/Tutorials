#ifndef __FIGURE_H__
#define __FIGURE_H__

class Figure{
public:
    virtual ~Figure(){};
    virtual void afficher_info()const=0;
    virtual float perimetre()const=0;
    virtual float surface()const=0;
};

#endif//__FIGURE_H__
