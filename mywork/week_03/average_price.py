from books_function import get_books

books = get_books()
print(books)
total = 0
count = 0

for book in  books:
    # At least one of the books doesn't have a price, so we need to check if the price exists before adding it to the total
    price = book.get('price')
    # To handle null values, we can check if the price is an instance of int or float before adding it to the total
    total += isinstance(price, (int,float))
    count += 1
average = total / count
print(f'The average price of books is {average}')
