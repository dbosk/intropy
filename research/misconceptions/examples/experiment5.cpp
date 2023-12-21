#include <iostream>

class TraceClass {
	public:
	TraceClass() {
		std::cout << this << " object created" << std::endl;
	}
};

void test_function(TraceClass obj=TraceClass()) {
	std::cout << "test_function called" << std::endl;
}

int main(void) {
	std::cout << "test code starts" << std::endl;
	test_function();
	test_function();

	return 0;
}
