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

# Membuat objek Bookstore
bookstore = Bookstore("Toko Buku ABC")

# Menggunakan sistem input untuk menambahkan buku ke dalam toko
n = int(input("Inputkan jumlah buku yang ingin ditambahkan: "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")
    price = float(input("Harga: "))

    book = Book(title, author, price)
    bookstore.add_book(book)

# Menampilkan daftar buku yang tersedia di toko
bookstore.display_books()
