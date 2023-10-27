import json
from models import Author, Quote
from db import connect

connect()

with open('authors.json', 'r', encoding='utf-8') as authors_file:
    authors_data = json.load(authors_file)

for author_data in authors_data:
    author_name = author_data['fullname']
    existing_author = Author.objects(fullname=author_name).first()

    if not existing_author:
        author = Author(**author_data)
        author.save()

with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
    quotes_data = json.load(quotes_file)

for quote_data in quotes_data:
    author_name = quote_data['author']
    author = Author.objects(fullname=author_name).first()

    if not author:
        author = Author(fullname=author_name)
        author.save()

    quote_data['author'] = author
    quote = Quote(**quote_data)
    quote.save()
