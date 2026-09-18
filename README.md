# Python for Data Science

Five modules from the 42 Python for Data Science Piscine, progressing from Python fundamentals to NumPy, pandas, visualisation, and object-oriented design.

| Module | Topics | Subject |
| --- | --- | --- |
| [Starting](0-starting/) | Types, command-line input, generators, and Python packaging | [PDF](subject/python-0-starting.pdf) |
| [Array](1-array/) | NumPy arrays, image manipulation, transposition, and colour filters | [PDF](subject/python-1-array.pdf) |
| [DataTable](2-datatable/) | CSV loading, pandas transformations, and Matplotlib visualisation | [PDF](subject/python-2-datatable.pdf) |
| [OOP](3-oop/) | Abstract classes, inheritance, properties, and operator overloading | [PDF](subject/python-3-oop.pdf) |
| [Data-Oriented Design](4-dod/) | Statistics, closures, decorators, and dataclasses | [PDF](subject/python-4-dod.pdf) |             |

## Running the exercises

Use Python 3.10+ in a virtual environment. For example:

```bash
python -m pip install -r 1-array/requirements.txt
cd 1-array/ex00
python tester.py
```

Scripts should be run from their exercise directories so local datasets and images resolve correctly. The first three modules have their own `requirements.txt`; the OOP and Data-Oriented Design modules use only the standard library.
