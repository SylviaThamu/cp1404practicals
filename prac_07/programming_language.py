"""
CP1404/CP5632 Practical - Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic
        self.year = year

    def __str__(self):
        """Return user-friendly string for a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, "
                f"First appeared in {self.year}")

    def is_dynamic(self):
        """Return True if language is dynamically typed."""
        return self.typing == "Dynamic"
