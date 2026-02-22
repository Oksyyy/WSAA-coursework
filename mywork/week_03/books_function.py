import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def get_books():
    response = requests.get(url)
    return response.json()

def book_by_id(book_id):
    url_id = url+ "/" + str(book_id)
    response = requests.get(url_id)
    return response.json()

def crete_book(newbook):
    response = requests.post(url, json=newbook)
    return response.json()

def update_book(book_id, book_diff):
    update_url = url + "/" +str(book_id)
    response = requests.put(update_url, json=book_diff)
    return response.json()

def delete_book(book_id):
    delete_url = url + "/" + str(book_id)
    response = requests.delete(delete_url)
    return response.json()

if __name__ == "__main__":
    #print(get_books())
    #print(book_by_id(1558))
    newbook = {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'price': 18.95
    }
    #print(crete_book(newbook))
    book_diff = {
        'price':24
    }
    #print(update_book(1679, book_diff))
    print(delete_book(1679))