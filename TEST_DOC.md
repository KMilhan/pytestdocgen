Test case documentation
========================
<div style="text-align: right"><p>version: UTC 2019-05-08 04:43:07</p></div>

#### Test Page: gendoc
###### Test Case: tc to markdown

* **Location**
    - `tests/test_gendoc.py`@`9:0 - 22:0`

* **Summary**

  **Convert a test case to markdown string**

* **Signature and asserts**
  ```python
  def test_tc_to_markdown():
      assert tc_to_markdown(tc) is not None
  ```
###### Test Case: gendoc

* **Location**
    - `tests/test_gendoc.py`@`24:0 - 30:0`

* **Summary**

  **Convert a test directory to markdown document**

* **Signature and asserts**
  ```python
  def test_gendoc():
      assert md is not None
  ```
#### Test Page: load
###### Test Case: file model

* **Location**
    - `tests/test_load.py`@`9:0 - 28:0`

* **Summary**

  **Test if file model is created**

* **Signature and asserts**
  ```python
  def test_file_model():
      assert TestFile(compos_file, test_root) is not None
      assert (
      assert len(TestFile(compos_file, test_root).test_cases[3].decorators) == 2
  ```
###### Test Case: dir model

* **Location**
    - `tests/test_load.py`@`30:0 - 36:0`

* **Summary**

  **Test if directory model is created**

* **Signature and asserts**
  ```python
  def test_dir_model():
      assert td is not None
      assert td.test_cases is not None
  ```
###### Test Case: find all files

* **Location**
    - `tests/test_load.py`@`38:0 - 42:0`

* **Summary**

  **Test if all test files with a given pattern are found**

* **Signature and asserts**
  ```python
  def test_find_all_files():
      assert len([x for x in find_all_test_files(test_root)]) == 4
  ```
#### Test Page: conf
###### Test Case: pyproject toml

* **Location**
    - `tests/test_conf.py`@`6:0 - 15:0`

* **Summary**

  **Test load and parsing of pyproject.toml configuration file**

* **Signature and asserts**
  ```python
  def test_pyproject_toml():
      assert config["--format"] == "markdown"
  ```
#### Test Page: gdocstring
###### Test Case: simple parse

* **Location**
    - `tests/test_gdocstring.py`@`7:0 - 13:0`

* **Summary**

  **Test the simplest docstring parse**

* **Signature and asserts**
  ```python
  def test_simple_parse():
      test_string = '''"""async coro"""'''
      assert gd.summary == "async coro"
  ```
###### Test Case: simple parse2

* **Location**
    - `tests/test_gdocstring.py`@`15:0 - 23:0`

* **Summary**

  **Test the simplest docstring parse with an unconventional whitespace**

* **Signature and asserts**
  ```python
  def test_simple_parse2():
      async coro
      assert gd.summary == "async coro"
  ```
###### Test Case: parse

* **Location**
    - `tests/test_gdocstring.py`@`25:0 - 83:0`

* **Summary**

  **Test docstring parse with full possibilities**

* **Signature and asserts**
  ```python
  def test_parse():
      assert gd.summary == "Test if addition is a part of summation"
      assert gd.description == (
      assert gd.sections["Returns"] == "None as this is a test"
      assert gd.sections["Expected Output"] == "Summation"
      assert gd.sections["Note"] == "This test is not enough to test summation"
      assert (
      assert (
  ```
###### Test Case: section name and content extraction

* **Location**
    - `tests/test_gdocstring.py`@`85:0 - 95:0`

* **Summary**

  **Does section name and content of it gets separated properly?**

* **Signature and asserts**
  ```python
  def test_section_name_and_content_extraction():
      assert name == "Input"
      assert content == "Any Integer which you can see pretty much everyday"
  ```
*documentation created by PyTestDocGen@UTC 2019-05-08 04:43:07*
