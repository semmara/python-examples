#include "foo.h"

#include <boost/python.hpp>
BOOST_PYTHON_MODULE(libfoo) {
	using namespace boost::python;
	def("foo", foo);
	def("foo2", foo2);
}

