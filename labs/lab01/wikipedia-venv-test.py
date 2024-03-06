import wikipedia

article_name = input("Enter article name: ")
page = wikipedia.page(article_name)
summary = page.summary
url = page.url

print(f"Summary: {summary}\nUrl: {url}")