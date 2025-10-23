"""Custom exceptions for file parser"""


class FileParserError(Exception):
    """Base exception for all file parser errors."""
    pass

class FileReadError(FileParserError):
    """Raised when file cannot be read."""
    pass

class ParseError(FileParserError):
    """Raised when content cannot be parsed."""

class ValidationError(FileParserError):
    """Raised when data validation fails."""
    pass

class TransformationError(FileParserError):
    """Raised when data transformation fails."""
    pass