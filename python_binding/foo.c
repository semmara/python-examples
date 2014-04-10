#include <stdio.h>
#include "foo.h"
#include "foo_structs.h"

int foo() {
	printf("foo called\n");
	return 123;
}

int foo2(const int a, const int b) {
	int i;
	i = a * a + b; // something
	return i;
}

struct foofoo foo3() {
	struct foofoo f;
	f.i = 21;
	f.d = 345.543;
	f.c = 'r';
	return f;
}

void print_foofoo(struct foofoo ff) {
	printf("i: %d\n", ff.i);
	printf("d: %lf\n", ff.d);
	printf("c: %c\n", ff.c);
}

