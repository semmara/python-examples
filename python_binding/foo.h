#ifndef _FOO_H__
#define _FOO_H__

#ifdef __cplusplus
extern "C" {
#endif

struct foofoo;

int foo();
int foo2(const int, const int);
struct foofoo foo3();
void print_foofoo(struct foofoo);
char *foo4();

#ifdef __cplusplus
}
#endif

#endif // _FOO_H__
