Test case documentation
========================
<div style="text-align: right"><p>version: UTC 2019-05-08 04:42:32</p></div>


***
# integration

#### Test Page: composite
###### Test Case: addition and subtraction is the opposite

* **Location**
    - `tests/integration/test_composite.py`@`6:0 - 16:0`

* **Summary**

  **Test if addition and subtraction are the opposite operation**

* **Description**

  Long description following the summary explaining the various stuffs

* Precondition

    All inputs are integers

* **Signature and asserts**
  ```python
  def test_addition_and_subtraction_is_the_opposite():
      assert sub(add(1, 2), 2) == 1
  ```
###### Test Case: add is part of sigma

* **Location**
    - `tests/integration/test_composite.py`@`19:0 - 47:0`

* **Summary**

  **Test if addition is a part of summation**

* Steps

    * Add 0 in each iteration
  * Finish the iteration
  * Check if summation is zero

* Precondition

    All inputs are integers

* Input

    Any Integer

* Expected Output

    Summation

* Note

    This test is not enough to test summation

* Return

    None as this is a test

* **Decorated by**
    * `@pytest.mark.parametrize("test_input", [x for x in range(-2, 3)])`

* **Signature and asserts**
  ```python
  def test_add_is_part_of_sigma(test_input: int):
      assert add_res == sigma([1 for _ in range(test_input)])
  ```
###### Test Case: asyncio coro

* **Location**
    - `tests/integration/test_composite.py`@`50:6 - 54:0`

* **Summary**

  **Async coro**

* **Decorated by**
    * `@pytest.mark.asyncio`

* **Signature and asserts**
  ```python
   def test_asyncio_coro(x):
      assert bool(x)
  ```
###### Test Case: asyncio coro para

* **Location**
    - `tests/integration/test_composite.py`@`58:6 - 60:0`

* **Decorated by**
    * `@pytest.mark.asyncio`
    * `@pytest.mark.parametrize("x", [x for x in range(1, 3)])`

* **Signature and asserts**
  ```python
   def test_asyncio_coro_para(x):
      assert bool(x)
  ```

***
# unit

## composite_calc

#### Test Page: sigma
###### Test Case: sum of zero is zero

* **Location**
    - `tests/unit/composite_calc/test_sigma.py`@`4:0 - 6:0`

* **Signature and asserts**
  ```python
  def test_sum_of_zero_is_zero():
      assert sigma([0 for _ in range(1024)]) == 0
  ```
###### Test Case: sigma same values with opposite sign returns zero

* **Location**
    - `tests/unit/composite_calc/test_sigma.py`@`8:0 - 10:0`

* **Signature and asserts**
  ```python
  def test_sigma_same_values_with_opposite_sign_returns_zero():
      assert sigma([x for x in range(-2, 3)]) == 0
  ```
## simple_calc

#### Test Page: add
###### Test Case: addition operation returns addition

* **Location**
    - `tests/unit/simple_calc/test_add.py`@`6:0 - 8:0`

* **Signature and asserts**
  ```python
  def test_addition_operation_returns_addition():
      assert add(1, 2) == 1 + 2
  ```
###### Test Case: add same values with negative sign returns zero

* **Location**
    - `tests/unit/simple_calc/test_add.py`@`11:0 - 13:0`

* **Decorated by**
    * `@pytest.mark.parametrize("test_input", [x for x in range(-2, 3)])`

* **Signature and asserts**
  ```python
  def test_add_same_values_with_negative_sign_returns_zero(test_input: int):
      assert add(test_input, -test_input) == 0
  ```
#### Test Page: sub
###### Test Case: sub operation returns addition

* **Location**
    - `tests/unit/simple_calc/test_sub.py`@`6:0 - 8:0`

* **Signature and asserts**
  ```python
  def test_sub_operation_returns_addition():
      assert sub(1, 2) == 1 - 2
  ```
###### Test Case: sub same values returns zero

* **Location**
    - `tests/unit/simple_calc/test_sub.py`@`11:0 - 13:0`

* **Decorated by**
    * `@pytest.mark.parametrize("test_input", [x for x in range(-2, 3)])`

* **Signature and asserts**
  ```python
  def test_sub_same_values_returns_zero(test_input: int):
      assert sub(test_input, test_input) == 0
  ```
*documentation created by PyTestDocGen@UTC 2019-05-08 04:42:32*
