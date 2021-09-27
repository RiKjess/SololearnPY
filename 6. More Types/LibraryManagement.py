"""
Dictionary Functions


A library management program has a dictionary of books with their corresponding genres.

Take a book name as input and output the genre.
"""

books = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

if (book in books) == False:
    print("Not found")
else:
    print(books[book])