"""
write a program that prompts the user for a page title or search phrase, then prints some details of that page.
Use a loop that continues doing this until the user enters blank input.
"""
from wikipedia import wikipedia, DisambiguationError, PageError

title = input("Enter a page title: ")
while title != "":
    try:
        print(wikipedia.page(title).summary)
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(title))
    except PageError:
        'Page id "jcu" does not match any pages. Try another id!'
        print(f"Page id '{title}' does not match any pages. Try another id!")
    title = input("Enter a page title: ")
print("Thank you!")