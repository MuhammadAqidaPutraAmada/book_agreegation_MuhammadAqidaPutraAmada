# MANAJEMEN TOKO BUKU
Aplikasi Manajemen Toko Buku ini adalah tugas dari mata kuliah OOP, penulisan kode program menggunakan cara agreegation yang dimana setiap objek class Bookstore akan memiliki beberapa objek class Book.
## Penjelasan Program
#### Pembuatan Class Book :
Class Book memiliki beberapa atribut, yaitu self.title (untuk input judul buku), self.author (untuk input author buku), self.price (untuk input harga buku).
```sh
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
```
#### Pembuatan Class Bookstore:
Class Bookstore memiliki beberapa atribut, yaitu self.name dan self.books.
```sh
class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []
```
##### method add_book
untuk menambahkan data input dari Class Book ke dalam list self.books
```sh
def add_book(self, book):
        self.books.append(book)
```
##### method display_books
menggunakan for loop untuk menampilkan output daftar buku sesuai data input dari Class Book yang tersimpan dalam list self.books.
```sh
def display_books(self):
        print(f"Daftar Buku di {self.name}:")
        for book in self.books:
            print(f"Judul: {book.title}")
            print(f"Penulis: {book.author}")
            print(f"Harga: Rp {book.price}")
            print("")
```
##### membuat objek bookstore

```sh
bookstore = Bookstore("Toko Buku ABC")
```

##### membuat sistem input
menggunakan for loop untuk membuat sistem input menambahkan buku. data input akan dikirimkan ke Class Book melalui kode: 
"book = Book(title, author, price)
bookstore.add_book(book)"
```sh
n = int(input("Inputkan jumlah buku yang ingin ditambahkan: "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")
    price = float(input("Harga: "))

    book = Book(title, author, price)
    bookstore.add_book(book)

```

##### membuat display output
menampilkan output dengan memanggil method display_books() dari Class Bookstore
```sh
bookstore.display_books()
```
