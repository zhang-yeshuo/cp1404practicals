import wikipedia


def wikipedia_page():
    while True:
        answer = input("Enter page title:  ")
        if not answer:
            break
        try:
            page = wikipedia.page(answer, auto_suggest=False)
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
            continue
        except wikipedia.PageError:
            print("Error: Page not found.")
        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    wikipedia_page()