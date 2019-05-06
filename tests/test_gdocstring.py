from pytestdocgen.gdocstring import (
    RelaxedGoogleDocstring,
    separate_section_content,
)


def test_simple_parse():
    """Test the simplest docstring parse"""
    test_string = '''"""async coro"""'''

    gd = RelaxedGoogleDocstring(test_string)
    assert gd.summary == "async coro"


def test_simple_parse2():
    """Test the simplest docstring parse with an unconventional whitespace"""
    test_string = '''"""
    async coro
    """'''

    gd = RelaxedGoogleDocstring(test_string)
    assert gd.summary == "async coro"


def test_parse():
    """Test docstring parse with full possibilities"""
    test_string = '''"""
Test if addition is a part of summation

Certainly long long description we have in here for the good
test across multiple lines we have description

    * Like this
    * And
    * That

Steps:
    * Add 0 in each iteration
    * Finish the iteration
    * Check if summation is zero

Precondition:
    All inputs are integers

Input: Any Integer which you can see pretty much
    tous-les-jours

Expected Output:
    Summation

Note:
    This test is not enough to test summation

Returns:
    None as this is a test
"""
'''

    gd = RelaxedGoogleDocstring(test_string)

    assert gd.summary == "Test if addition is a part of summation"
    assert gd.description == (
        "Certainly long long description we have in here for the good\n"
        "test across multiple lines we have description\n"
        "\n"
        "    * Like this\n"
        "    * And\n"
        "    * That"
    )
    assert gd.sections["Returns"] == "None as this is a test"
    assert gd.sections["Expected Output"] == "Summation"
    assert gd.sections["Note"] == "This test is not enough to test summation"
    assert (
        gd.sections["Input"]
        == "Any Integer which you can see pretty much tous-les-jours"
    )
    assert (
        gd.sections["Steps"]
        == """* Add 0 in each iteration
* Finish the iteration
* Check if summation is zero"""
    )


def test_section_name_and_content_extraction():
    """Does section name and content of it gets separated properly?"""
    test_section = """Input: Any Integer which you can see pretty much
    everyday
"""

    name, content = separate_section_content(test_section.splitlines())

    assert name == "Input"
    assert content == "Any Integer which you can see pretty much everyday"
