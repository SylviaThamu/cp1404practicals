"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        musicians_text = ", ".join(musician_strings)
        return f"{self.name} ({musicians_text})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing (or needing) an instrument."""
        lines = []
        for musician in self.musicians:
            lines.append(musician.play())
        return "\n".join(lines)
