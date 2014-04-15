#include "foo.h"
#include "foo_structs.h"

#include <Python.h>
#include <string>

std::string wrap_foo4() {
	std::string s;
	char *r = foo4();
	if (!r)
		return NULL;
	s.assign(r);
	return s;
}

#include <boost/python.hpp>
BOOST_PYTHON_MODULE(libfoo) {
	using namespace boost::python;
	class_<foofoo>("foofoo");
	def("foo", foo);
	def("foo2", foo2);
	def("foo3", foo3);
	def("p_ff", print_foofoo);
	def("foo4", wrap_foo4);
}

