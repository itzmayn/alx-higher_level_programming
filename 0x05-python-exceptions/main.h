#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <Python.h>

/* Function to print information about a Python list */
void print_python_list(PyObject *p);

/* Function to print information about a Python bytes object */
void print_python_bytes(PyObject *p);

/* Function to print information about a Python float object */
void print_python_float(PyObject *p);

#endif /* MAIN_H */