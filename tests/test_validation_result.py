"""Tests for ValidationResult model."""
from file_parser.models.validation_result import ValidationResult

class TestValidationResult:
    """Test cases for ValidationResult class."""

    def test_valid_result(self):
        """Test creating a valid result."""
        result = ValidationResult(is_valid=True, errors=[])
        assert result.is_valid
        assert len(result.errors) == 0

    def test_invalid_result_single_error(self):
        """Test creating invalid result with one error."""
        result = ValidationResult(
            is_valid=False,
            errors=["Missing required field 'name'"]
        )
        assert not result.is_valid
        assert len(result.errors) == 1
        assert "Missing required field" in result.errors[0]

    def test_invalid_result_multiple_errors(self):
        """Test creating invalid result with multiple errors."""
        errors = [
            "Row 1: Missing field 'age'",
            "Row 2: Invalid type for 'age'"
        ]
        result = ValidationResult(is_valid=False, errors=errors)
        assert not result.is_valid
        assert len(result.errors) == 2

    def test_string_representation_valid(self):
        """Test string representation of valid result."""
        result = ValidationResult(is_valid=True, errors=[])
        assert "passed" in str(result).lower()

    def test_string_representation_invalid(self):
        """Test string representation of invalid result."""
        result = ValidationResult(
            is_valid=False,
            errors=["Error 1", "Error 2"]
        )
        result_str = str(result)
        assert "failed" in result_str.lower()
        assert "2 error" in result_str.lower()

    def test_errors_list_is_mutable(self):
        """Test that errors list can be accessed and iterated."""
        errors = ["Error 1", "Error 2", "Error 3"]
        result = ValidationResult(is_valid=False, errors=errors)

        # Should be able to iterate
        count = 0
        for error in result.errors:
            count += 1
        assert count == 3

        # Should be able to access by index
        assert result.errors[0] == "Error 1"
        assert result.errors[2] == "Error 3"

    def test_empty_errors_list_for_valid_result(self):
        """Test that valid results have empty error lists."""
        result = ValidationResult(is_valid=True, errors=[])
        assert result.errors == []
        assert len(result.errors) == 0