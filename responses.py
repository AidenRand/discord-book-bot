import json

from urllib.request import urlopen

def make_response(message):
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    isbn = message.strip()

    # recieve json book data from api
    resp = urlopen(api + isbn)
    book_data = json.load(resp)

    # create variables for responses
    book_info = book_data['items'][0]['volumeInfo']
    author = book_info['authors']
    clean_author = author if len(author) > 1 else author[0]

    # display title, author, page count, pub date
    title_res = f"\nTitle: {book_info['title']}"
    author_res = f"\nAuthor: {clean_author}"
    page_count_res = f"\nPage count: {book_info['pageCount']}"
    pub_date_res = f"\nPublication date: {book_info['publishedDate']}"

    # concat all responses into one
    wholeResponse = title_res + author_res + page_count_res + pub_date_res

    return str(wholeResponse)