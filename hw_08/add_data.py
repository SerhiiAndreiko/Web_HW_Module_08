import json
from models import Author, Quote
from mongoengine import connect, disconnect

try:
    connect('my_database', host='mongodb+srv://fantom:fantomDB@cluster0.xbtnffb.mongodb.net/test?retryWrites=true')

    with open('authors.json', 'r', encoding='utf-8') as authors_file:
        authors_data = json.load(authors_file)

    for author_data in authors_data:
        author_name = author_data.get('fullname')
        if author_name:
            existing_author = Author.objects(fullname=author_name).first()

            if not existing_author:
                author = Author(**author_data)
                author.save()

    with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
        quotes_data = json.load(quotes_file)

    for quote_data in quotes_data:
        author_name = quote_data.get('author')
        if author_name:
            author = Author.objects(fullname=author_name).first()

            if not author:
                author = Author(fullname=author_name)
                author.save()

            quote_data['author'] = author
            quote = Quote(**quote_data)
            quote.save()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    disconnect()  
