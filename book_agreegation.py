class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Daftar Buku di {self.name}:")
        for book in self.books:
            print(f"Judul: {book.title}")
            print(f"Penulis: {book.author}")
            print(f"Harga: Rp {book.price}")
            print("")


bookstore = Bookstore("Toko Buku ABC")

# I N P U T
n = int(input("Inputkan jumlah buku yang ingin ditambahkan: "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")
    price = float(input("Harga: "))

    book = Book(title, author, price)
    bookstore.add_book(book)

# D I S P L A Y
bookstore.display_books()
