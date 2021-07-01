class Academic:
    def __init__(self, name):
        self.name = name
        self.papers = []

alice = Academic('Alice')
print(alice.name)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

def __str__(self):
        return self.title + ' by ' + self.author

book = Book('A Book', 'Me')

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

class Library:
    def __init__(self):
        self.books = []



    def add_book(self, title, author):
        self.books.append(Book(title, author))


    def __len__(self):
        return len(self.books)

    def __getitem__(self, key):
        return self.books[key]

    def by_author(self, author):
        matches = []
        for book in self.books:
            if book.author == author:
                matches.append(book)

        if not matches:
            raise KeyError('Author does not exist')

        return matches


    @property
    def titles(self):
        titles = []
        for book in self.books:
            titles.append(book.title)

        return titles

    @property
    def authors(self):
        authors = []
        for book in self.books:
            if book.author not in authors:
                authors.append(book.author)

        return authors


library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

#books = library.by_author('Carol')

from functools import reduce

def sum_of_squares(l):
    squares = [x * x for x in l]
    return reduce(lambda a, b: a + b, squares)


print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))