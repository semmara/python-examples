#include <stdio.h>
#include "foo.h"

int foo() {
	printf("foo called\n");
	return 123;
}

int foo2(const int a, const int b) {
	int i;
	i = a * a + b; // something
	return i;
}

