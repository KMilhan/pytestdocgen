"""This will give you a paper you read before an important test"""

from pathlib import Path

from setuptools import find_packages, setup

short_desc = "A rather formal documentation generator for python test suite"
readme_path = Path(__file__).parent / "README.md"

setup(
    author="Milhan KIM",
    author_email="kimmilhan@gmail.com",
    name="pytestdocgen",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"pytestdocgen": ["templates/**"]},
    description=short_desc,
    long_description=readme_path.read_text(),
    zip_safe=False,
    install_requires=["parso", "cchardet", "jinja2", "docopt", "toml"],
    test_require=["pytest"],
    test_suite="tests",
    python_require=">=3.7",
    entry_points={
        "console_scripts": ["pytestdocgen = pytestdocgen.__main__:run"]
    },
)
