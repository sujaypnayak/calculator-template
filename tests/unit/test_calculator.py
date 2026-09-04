"""
Unit Tests for Calculator
"""

import pytest
from src.calculator import add, divide, multiply, subtract


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestMultiplyDivide:
    """Test multiplication and division logic, zero cases, and edge cases."""

    def test_multiply_basic(self):
        """Test standard multiplication with positive and negative numbers."""
        assert multiply(4, 3) == 12
        assert multiply(-2, 5) == -10

    def test_divide_basic(self):
        """Test standard division."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide 10 by zero"):
            divide(10, 0)
