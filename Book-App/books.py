from fastapi import Body, FastAPI, Path, Query, HTTPException
from Book import Book, BookRequest
from starlette import status


app = FastAPI(
    title='Book Application for WebNet Inc.',
    description= 'This is a book management api',
    version= '0.0.0.1',
    terms_of_service= 'Terms and conditions applies',
    contact= {
        'name' : 'Azeez Bammeke',
        'url' : 'http://www.linkedin.com',
        'email' : 'azeez.bammeke@gmail.com'
    }
)


BOOKS = [
    Book(1, 'Title One', 'Author One', 'science book', 5, 2021),
    Book(2, 'Title Two', 'Author Two', 'history book', 3, 2024),
    Book(3, 'Title Three', 'Author Three', 'science book', 4, 2020),
    Book(4, 'Title Four', 'Author Four', 'math book', 3, 2010),
    Book(5, 'Title Five', 'Author Five', 'math book', 2, 2021),
    Book(6, 'Title Six', 'Author Six', 'math book', 4, 2020),
]


@app.get('/books', status_code=status.HTTP_200_OK)
async def get_all_books():
    return BOOKS


@app.get('/find-book/{id}', status_code=status.HTTP_200_OK)
async def get_book_by_id(id: int = Path(gt = 0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail='Item not found: ' + str(id)) 

@app.get('/books/published/', status_code=status.HTTP_200_OK)
async def get_book_by_published_date(published_date: int = Query(gt= 1999, lt=2024)):
    found_books = []
    for book in BOOKS:
        if book.published_date == published_date:
            found_books.append(book)
    return found_books


@app.get('/books-by-category/{category}', status_code=status.HTTP_200_OK)
async def get_books_by_category(category: str):
    found_books = []
    for book in BOOKS:
        if book['category'].casefold() == category.casefold():
            found_books.append(book)
    return found_books


@app.get('/books-by-rating/', status_code=status.HTTP_200_OK)
async def get_books_by_category(rating_number: int = Query(gt =0, lt= 6)):
    found_books = []
    for book in BOOKS:
        if book.rating == rating_number:
            found_books.append(book)
    return found_books      


@app.post('/book', status_code=status.HTTP_201_CREATED)
async def add_book(book: BookRequest):
    new_book = Book(**book.model_dump())
    BOOKS.append(find_book_id(new_book))



@app.put('/book/update', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(updated_book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == updated_book.id:
            BOOKS[i] = update_book
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code= 404, detail='Book not found')    


@app.delete('/book/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(id: int = Path(gt = 0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            book = BOOKS.pop(i)
            book_changed = True
            return book
    if not book_changed:
        raise HTTPException(status_code=404, detail='Book not found: ' + str(id))    



def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

""""
{
"title": "People's Book",
"author": "Author One",
"category": "science"
}
"""