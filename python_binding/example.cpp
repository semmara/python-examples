/* This is just TESTCODE. It should not be used for productiv. */

#include <iostream>
class Mensch {
    public:
        Mensch() {
            std::cout << "Mensch init" << std::endl;
        }
        void sein(bool b) {
            if (b)
                std::cout << "sein" << std::endl;
            else
                std::cout << "nicht sein" << std::endl;
        }
};

#include <boost/python.hpp> 
BOOST_PYTHON_MODULE(libmensch) {
    using namespace boost::python;
    class_<Mensch>("Mensch", init<>())
        .def("sein", &Mensch::sein)
    ;
}
 
