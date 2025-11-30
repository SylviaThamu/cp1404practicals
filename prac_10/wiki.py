"""CP1404 Practical 10 - Wikipedia API example."""
import wikipedia


def main():
    """Get Wikipedia page details based on user input."""
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except wikipedia.exceptions.DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)
        print()
        title = input("Enter page title: ")
    print("Thank you.")


if __name__ == '__main__':
    main()