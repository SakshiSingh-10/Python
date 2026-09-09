class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            print("Book not found")
            return

        if member_id not in self.members:
            print("Member not found")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.available:
            print("Book is already issued")
            return

        book.available = False
        member.borrowed_books.append(book_id)

        print("Book issued successfully")

    def return_book(self, book_id, member_id):
        book = self.books[book_id]
        member = self.members[member_id]

        if book_id in member.borrowed_books:
            member.borrowed_books.remove(book_id)
            book.available = True
            print("Book returned successfully")
        else:
            print("This member did not issue this book")