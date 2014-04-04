#include <boost/python.hpp>

/* This is just TESTCODE. It should not be used for productiv. */

class Test {
	public:
		int add(const int, const int);
		int mul(const int, const int);
};

 int Test::add(const int a, const int b) {
    return a+b;
 }
 
 int Test::mul(const int a, const int b) {
    return a*b;
 }
 
 BOOST_PYTHON_MODULE(helloext) {
    using namespace boost::python;
    class_<Test>("Test", init<>())
    .def("add", &Test::add)
    .def("mul", &Test::mul)
    ;
 }
 
