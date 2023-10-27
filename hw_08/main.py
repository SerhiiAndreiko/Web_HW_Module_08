from db import connect
from models import Author, Quote
from redis_cache import cache

connect()

@cache
def search_quotes(query: str):
    if query.startswith('name: '):
        author_name = query[6:]
        author = Author.objects(fullname__icontains=author_name).first()
        if author:
            return Quote.objects(author=author)
        else:
            return []
    elif query.startswith('tag:'):
        tag = query[4:]
        return Quote.objects(tags__icontains=tag)
    elif query.startswith('tags:'):
        tags = query[5:].split(',')
        return Quote.objects(tags__in=tags)
    else:
        return []

def print_quote(quote):
    print(f'Author: {quote.author.fullname}')
    print(f'Tags: {", ".join(quote.tags)}.')
    print(f'Quote: {quote.quote}')

if __name__ == '__main__':
    while True:
        user_input = input('Enter command: ').lower()
        if user_input == 'exit':
            break

        quotes = search_quotes(user_input)
        if not quotes:
            print("No matching quotes found.")
        else:
            for quote in quotes:
                print_quote(quote)
