#include "main.h"

/* Function to print information about a Python list */
void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *item_type = item->ob_type->tp_name;

        printf("Element %ld: %s\n", i, item_type);
    }
}

/* Function to print information about a Python bytes object */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size = PyBytes_GET_SIZE(p);
    Py_ssize_t i;
    const char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

/* Function to print information about a Python float object */
void print_python_float(PyObject *p) {
    double value = PyFloat_AsDouble(p);

    if (PyErr_Occurred() != NULL) {
        printf("[.] float object info\n");
        printf("  [ERROR] Invalid Float Object\n");
        PyErr_Clear();
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
