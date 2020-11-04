import os
import sys

from setuptools import setup, find_packages

import versioneer
from distutils.sysconfig import get_python_lib


setup(
    name="clx",
    version=versioneer.get_version(),
    description="CLX",
    author="NVIDIA Corporation",
    packages=find_packages(include=["clx", "clx.*"]),
    package_data={
        "clx.analytics": ["resources/*.txt"],
        "clx.parsers": ["resources/*.yaml"],
        "clx.dns": ["resources/*.txt"],
        "clx.heuristics": ["resources/*.csv"]
    },
    license="Apache",
    cmdclass=versioneer.get_cmdclass()
)
