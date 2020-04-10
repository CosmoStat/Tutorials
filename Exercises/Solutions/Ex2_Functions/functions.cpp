#include <iostream>

using namespace std;

void func1(int a){

	a += 2;

}

void func2(int *a){

	*a += 2;

}

void func3(int &a){

a += 2;

}


int main()
{
  int myA = 3;

  cout << "myA = " << myA << endl;

  func1(myA);
  cout << "after call func1, myA = " << myA << endl;

  func2(&myA);
  cout << "after call func2, myA = " << myA << endl;

  func3(myA);
  cout << "after call func3, myA = " << myA << endl;

  return 0;
}
