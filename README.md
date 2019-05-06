PyTestDocGen - write test code and doc in the same place!
=====

A rather formal document generator for the python unittest framework based test 
suites

## This project is under initial development...
### A lot more is coming
* Command line tool
* Excel file export
* A comprehensive documentation on how to use...

## Example
See [EXAMPLE.md](EXAMPLE.md) made out of [test_package](test_package/)

## How to use
### How to organize your tests and documentize them
* Your directory schema is your test document structure
    - Directory structure becomes section-subsuction-subsubsection-page relation
        * Any directory can have test case though
    - Use maximum 4 depth of directories
    - This is the only way to organize the section structure

* __This program is all about the docstring.__
    - Write down docstring in every test case in the following fashion
    ```python
    @YOUR_DECORATOR_IS_DOCUMENTED_TOO
    def test_THIS_IS_YOUR_TEST_CASE_NAME():
    """
    SUMMARY_OF_YOUR_TEST. This can be multiline
    string, and program will concatenate the lines. After summary, please
    put one white line
    
    LONG_DESCRIPTION_OF_YOUR_TEST_CASE.
    This can be multiline markdown
        * Like
        * This
        * Of course you can omit description, or both summary and description
    
    TC_FIELD_NAME:
        * Field name always starts with capital letter and ends with `:`
        * Content can be markdown
        * Use as many section as you want, the program will organize them later
        * All the other usual Google Docstring sections will be treated as
        * Below field is an example
    
    Expected Input:
        All inputs are integers
    
    """
        pass
    ```

### Trigger the generation
Try 
```bash
> pytestdocgen
```
after installation.

### Configuration
We provide two ways of configuration
1. Configuration over arguments
1. Configuration over [pyproject.toml](https://www.python.org/dev/peps/pep-0518/)

#### Configuration over arguments
For more on the usage, try
```bash
> pytestdocgen -h

Welcome to PyTestDocGen 🎴

Usage:
  pytestdocgen [--src-dir=SRC_DIR] [--format=FORMAT] [--test-dir=TEST_DIR] 
  [--output=FILE] [--test-prefix=PREFIX] [--header=<str>] [--footer=<str>]
  pytestdocgen (-h | --help)

Options:
  -h --help                 Show this screen.
  -s --src-dir=SRC_DIR      Working directory, usually a root of source code [default: .]
  -f --format=FORMAT        Format of the output file [default: markdown]
  -t --test-dir=TEST_DIR    Directory of tests, relative to SRC_DIR [default: tests]
  -o --output=FILE          Output file path [default: TEST_DOC.md]
  -p --test-prefix=PREFIX      Custom test file prefix [default: test_]

  --header=<str>            Custom header to provide
  --footer=<str>            Custom footer to provide
>
```

#### Configuration over [pyproject.toml](https://www.python.org/dev/peps/pep-0518/)
Use the same arguments as you pass via commandline in aforementioned part.

Note,
1. Use `tool.pytestdocgen` section in `toml`.
1. Omit `--` in the beginning of the argument name. e.g., `--src-dir` in a shell is equivalent to
`src-dir` in toml file.
For example,
```toml
[tool.pytestdocgen]
src-dir = '.'
format = 'markdown'
test-dir = 'tests'
output = 'TEST_DOC.md'
```

## PyTestDocGen is/does...
* Translate Google Docstring for tests into organized documentation
* Guarantees *test doc* - *test code* traceability as you type in a same 
place. Similar to [doctest](https://docs.python.org/3/library/doctest.html).

## PyTestDocGen is not...
* An API documentation generator like [Sphinx](http://www.sphinx-doc.org)
* A replacement to the TCMS

## Motivation
* I could not afford to have a license of TCMS. Neither I had a time to learn
 one of them 😔
* I had a spreadsheet file in shared directory to manage test cases.
    - the biggest problem is *test doc* - *test code* traceability.
        * Which updated and where we should reflect?
    - test case and test documentation configuration management brought a 
    huge amount of communication
* We read test doc more often than we actually run test because we had
    - not frequently modified test cases
    - high turnover-rate of developers
    - 💡 low learning curve with familiar toolkits

## Alternatives
If you are looking for an API documentation generator, there are great OSS 
solutions already
* [Sphinx](http://www.sphinx-doc.org)
* [pdoc](https://github.com/mitmproxy/pdoc)

If you are looking for a test case management system that fits to your 
requirements, OSS TCMSs are great alternatives
* [Kiwi TCMS](http://kiwitcms.org/)
* [Robot Framework](https://robotframework.org/)
