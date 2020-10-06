#include <iostream>
using namespace std;

int a = 10; // This is a 'global' (within namespace std) variable

namespace private_space {
	int a = -10; // This is the version of a defined inside namespace 'private_space'
}

int main() {
	cout << "Hi there! This is a C++ world" << endl;
	int a = 20; // this is a local (inside main) variable, within namespace 'std'
	cout << "Please enter some number: ";
	cout << "variable a (local) = " << a << endl; //prints 20
	cout << "variable a (global) = " << ::a << endl; //prints 10
	cout << "variable a (private_space) = " << private_space::a << endl; //prints -10
	return 0;
}
