class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            library.add_user(self)
            if self.username in library.rented_books:
                library.rented_books[self.username][book_name] = days_to_return
            else:
                library.rented_books[self.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, rented_books in library.rented_books.items():
            for book, days_to_return in rented_books.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self, author, book_name, library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.books_available[author].append(book_name)
            del(library.rented_books[self.username][book_name])
            return
        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"