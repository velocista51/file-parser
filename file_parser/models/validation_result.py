"""
    Data models for validation results.
    Will create a result object to return two pieces of information.
    1) Did it pass or fail? (Boolean)
    2) What whent wront? (list of error messages)
"""
from typing import List  # import List for type hints
from dataclasses import dataclass  # import dataclass decorator for automatic method generation


@dataclass  # decorator that generates __init__, __repr__, __eq__ dunder methods automatically
class ValidationResult:
    """
    Result of data validation.

    Attributes:
        is_valid: True if validation passed, False otherwise
        errors: List of error messages (empty if is_valid=True)
    """
    is_valid: bool  # pass/fail Bool, type hint ensures only True/False can be assigned
    errors: List[str]  # List of error message strings, type hint ensures it is always list of strings

    def __str__(self) -> str:
        """String representation of validation result."""
        if self.is_valid:
            return "Validation passed"
        return f"Validation failed with {len(self.errors)} errors(s):\n" + \
                "\n".join(f" = {error}" for error in self.errors)


