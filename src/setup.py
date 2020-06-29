from distutils.core import setup

setup(
    name="flim",
    version="0.1",
    packages=["flim"],
    install_requires=[
        "attrs==19.3.0",
        "construct==2.10.56",
        "pypng==0.0.19",
    ],
)
