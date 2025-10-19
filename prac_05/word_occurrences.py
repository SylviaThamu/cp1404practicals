"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""


def main():
    """Count occurrences of words in user-entered text (basic version)."""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    for word, count in word_to_count.items():
        print(f"{word} : {count}")


main()
