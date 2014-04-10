#include "foo.h"
#include "foo_structs.h"

#include <boost/python.hpp>
BOOST_PYTHON_MODULE(libfoo) {
	using namespace boost::python;
	class_<foofoo>("foofoo");
	def("foo", foo);
	def("foo2", foo2);
	def("foo3", foo3);
	def("p_ff", print_foofoo);
}

