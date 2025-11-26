import os
import sys
from setuptools import Extension, find_packages, setup


# Project Information
DISTNAME = "deep-forest"
DESCRIPTION = "Deep Forest"
with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = "Simon Provost"
MAINTAINER_EMAIL = "simon.gilbert.provost@gmail.com"
URL = "https://github.com/LAMDA-NJU/Deep-Forest"
VERSION = "0.1.7"


if __name__ == "__main__":

    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(__file__))

    os.chdir(local_path)
    sys.path.insert(0, local_path)

    libraries = []
    if os.name == "posix":
        libraries.append("m")

    from Cython.Build import cythonize
    import numpy

    extensions = cythonize(
        [
            Extension(
                "deepforest._forest",
                sources=[os.path.join("deepforest", "_forest.pyx")],
                include_dirs=[numpy.get_include()],
                libraries=libraries,
                extra_compile_args=["-O3"],
            ),
            Extension(
                "deepforest._cutils",
                sources=[os.path.join("deepforest", "_cutils.pyx")],
                include_dirs=[numpy.get_include()],
                libraries=libraries,
                extra_compile_args=["-O3"],
            ),
            Extension(
                "deepforest.tree._tree",
                sources=[os.path.join("deepforest", "tree", "_tree.pyx")],
                include_dirs=[numpy.get_include()],
                libraries=libraries,
                extra_compile_args=["-O3"],
            ),
            Extension(
                "deepforest.tree._splitter",
                sources=[os.path.join("deepforest", "tree", "_splitter.pyx")],
                include_dirs=[numpy.get_include()],
                libraries=libraries,
                extra_compile_args=["-O3"],
            ),
            Extension(
                "deepforest.tree._criterion",
                sources=[os.path.join("deepforest", "tree", "_criterion.pyx")],
                include_dirs=[numpy.get_include()],
                libraries=libraries,
                extra_compile_args=["-O3"],
            ),
            Extension(
                "deepforest.tree._utils",
                sources=[os.path.join("deepforest", "tree", "_utils.pyx")],
                include_dirs=[numpy.get_include()],
                libraries=libraries,
                extra_compile_args=["-O3"],
            ),
        ]
    )

    for extension in extensions:
        extension.sources = [
            os.path.relpath(source, local_path) for source in extension.sources
        ]

    setup(
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        packages=find_packages(),
        include_package_data=True,
        description=DESCRIPTION,
        url=URL,
        version=VERSION,
        long_description=LONG_DESCRIPTION,
        zip_safe=False,
        ext_modules=extensions,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        python_requires=">=3.7",
        install_requires=[
            "numpy>=1.14.6,<2.0",
            "scipy>=1.1.0",
            "joblib>=0.11",
            "scikit-learn>=1.0,<1.6",
        ],
        setup_requires=["cython", "numpy>=1.21,<2.0"],
    )
