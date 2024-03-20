"""
Tests for module `main`
"""

from cimaging_python_template.main import my_function


def test_my_function():
    """
    Tests my function
    :return:
    """
    # With
    expected = "hello world"

    # When
    result = my_function()

    # Then
    assert result
