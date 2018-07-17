[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/drvinceknight/Python-Mathematics-Handbook/master)

# Doing mathematics with Python

- Aimed at Mathematicians with little to no Python knowledge.
- All documents are written as [Jupyter notebooks](./nbs/).

## Topics covered:

1. [Basic Python](./nbs/00-Studying-Mathematics-with-Python.ipynb)
2. [Using Sympy](./nbs/01-Symbolic-mathematics-with-Sympy.ipynb) for symbolic
   mathematics.
3. [Using Numpy](./nbs/02-Linear-algebra-with-Numpy.ipynb) for linear algebra.
4. [Using Pandas](./nbs/03-Data-analysis-with-Pandas.ipynb) for basic handling
   of data.

## Creating the pdfs and tex files:

Create the conda environment from the file:

    $ conda env create -f environment.yml

Source the conda environment:

    $ conda source pfm

Run the following command:

    $ inv main

## Testing the notebooks

It is possible to test that the notebooks run:

    $ inv test
