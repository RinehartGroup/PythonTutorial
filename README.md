# PythonTutorial

A Python tutorial focusing on analysis of magnetic data and other aspects relevant to the Rinehart Group.

## Setup

See [First Time Setup](docs/first_time_setup.md) for instructions on how to set up your development environment according to Rinehart group standards. The tutorials in this repository can be copied into your scratch repository made during the First Time Setup.

Alternatively you can fork this repository into your personal GitHub account and clone it from there. Use Python 3.10 to create your virtual environment and install required dependencies using

> pip install ipykernel git+https://github.com/RinehartGroup/MagnetoPy.git@v0.1.0

Here are some detailed instructions for [how to work with a forked version of this repository](docs/how_to_fork_this_repository.md).

## How to Use These Tutorials

The tutorials herein contain a mixture of background information, examples, and exercises. They assume some basic knowledge of Python. If you're new to Python you may want to practice some of the basics on [CheckiO](https://py.checkio.org/). Doing 2-3 of the modules there should be sufficient to get you started.

Similar to the exercises on CheckiO, the exercises in these tutorials ask for you to fill out a function definition given a function signature and return type. There are many ways to solve the same problem. Your work is ultimately checked using `assert` statements. `assert` statements raise an exception if the code following `assert` does not return `True`. For example, the following code will raise an exception:

```python
def get_average(a: float, b: float) -> float:
    return a + b

assert get_average(1, 2) == 1.5
# AssertionError
```

While the following code will not raise an exception:

```python
def get_average(a: float, b: float) -> float:
    return (a + b) / 2

assert get_average(1, 2) == 1.5
```

Completed tutorial notebooks can be found in [tutorial_answers](tutorial_answers).

## Tutorials

1. [Reading Files into DataFrames](tutorial/01_reading_files.ipynb)

   Read in some data from a .dat file containing data from magnetization vs field (hysteresis) measurements and do some basic manipulation of the data using `pandas`.

2. [Parsing Data Into Standard Formats](tutorial/02_parsing.ipynb)

   Having read in some .dat files containing data from M vs. H or ZFCFC experiments, figure out how to handle different file structures that arise from different users or different measurement conditions, and make some general functions that leave you with dataframes that are easy to plot and do analysis on.

3. [Object Oriented Programming and Documentation](tutorial/03_object_oriented_programming.ipynb)

   Use object oriented programming to organize the parsing code from previous tutorials into `DatFile` and `Dataset` classes. Document your code using docstrings.
