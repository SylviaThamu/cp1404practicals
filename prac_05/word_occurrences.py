"""
Word Occurrences
Estimate: 20 minutes
Actual:   26 minutes
"""


def main():
    """Count word occurrences."""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    width = max(len(word) for word in word_to_count)
    for word in sorted(word_to_count):
        print(f"{word:{width}} : {word_to_count[word]}")


main()
