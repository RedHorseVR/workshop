#include <iostream>
#include <stdexcept>

class Factorial {
		
	private:
		
	int factorial(int n) {
		if (n <= 1) {
		
			return 1;
		} else {
			
			return n * factorial(n - 1);
			}
		}
	public:
		
		Factorial() {
		for (int i = 2; i <= 8; i++) {
			try {
			
				std::cout << "Factorial of " << i << " = " << factorial(i) << std::endl;
			} catch (const std::overflow_error&) {
				std::cout << " !";
				std::cout << std::endl;
				}
			}
		
		}
		
	};
int main() {
	Factorial f;
	return 0;
}
//  Export  Date: 11:16:01 PM - 16:Jul:2025;

