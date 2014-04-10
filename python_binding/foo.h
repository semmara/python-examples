#ifdef __cplusplus
extern "C" {
#endif

struct foofoo;

int foo();
int foo2(const int, const int);
struct foofoo foo3();
void print_foofoo(struct foofoo);

#ifdef __cplusplus
}
#endif

