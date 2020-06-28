from distutils.core import setup

setup(
    name="flim",
    version="0.1",
    packages=["flim"],
    install_requires=[
        "attrs",
        "construct",
        "pypng",
    ],
)
