"""A package with tests"""

import os
from pathlib import Path

from setuptools import find_packages, setup

short_desc = (
    "A mock package for rather formal documentation generator for "
    "pytest suite"
)

setup(
    name="pytestdocgen",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    description=short_desc,
    zip_safe=False,
    test_require=["pytest", "pytest-asyncio"],
    test_suite="tests",
    python_require=">=3.7",
    entry_points={
        "console_scripts": [
            # 'jokbo_gen = pytestdocgen.__main__:run'
        ]
    },
)
