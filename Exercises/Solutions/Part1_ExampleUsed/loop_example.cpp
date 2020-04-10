// Sum of n numbers

#include <iostream>

using namespace std;

int main()
{
 int i, n, sum =0;
 
 std::cout << "enter the n number";
 std::cin >> n;
 
 i = 0;
 
 while(i<n) {
   sum = sum + i;
   i = i+ 1;
 }
 std::cout << "sum of first "<< n <<"numbers is: "<< sum << std::endl; 
 return 0;
}