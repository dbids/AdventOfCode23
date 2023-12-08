from setuptools import setup, find_packages

setup(
    name="advent-of-code-sample",
    version="0.1",
    description="dbids's solutions for https://adventofcode.com/",
    url="https://github.com/dbids/AdventOfCode23",
    author="dbids",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["dbids = days_pkg:mysolve"],
    },
)