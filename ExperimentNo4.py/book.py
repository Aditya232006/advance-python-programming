class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Available:", self.available)

b = Book("Python", "Guido", 2023)
b.display()
b.borrow()
b.display()
b.return_book()
b.display()