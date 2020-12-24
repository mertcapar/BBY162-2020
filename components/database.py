import sqlite3, os


class Book:
    def __init__(self, id, name, author, isbn):
        self.id = id
        self.name = name
        self.author = author
        self.isbn = isbn

    def is_empty(self):
        if self.name == "" or self.author == "":
            return True
        return False


class SqlLiteConnection:

    def __init__(self, path=str):

        if path.isspace() or path == '':
            raise ValueError("Bağlantı yolu hatalı girildi.")

        if not os.path.exists(path):
            raise FileExistsError("Veritabanı dosyası bulunamadı.")

        self.path = path
        self.database = None
        self.connected = False
        self.table = 'kitaplar'

    def connect(self):

        if self.connected:
            self.database.close()

        self.database = sqlite3.connect(self.path)
        self.cur = self.database.cursor()
        self.connected = True

    def disconnect(self):

        if not self.connected:
            raise Exception("Veritabanı zaten kapalı.")

        self.database.close()
        self.connected = False

    def read_all(self):
        if not self.connected:
            raise Exception("Veritabanı kapalı.")

        self.cur.execute("SELECT * FROM {0}".format(self.table))

        temp_list = []
        for data in self.cur.fetchall():
            p = Book(data[0], data[1], data[2], data[3])
            temp_list.append(p)

        return temp_list

    def add(self, book=Book):

        if not self.connected:
            raise Exception("Veritabanı kapalı.")

        if book.is_empty():
            raise Exception("Eklenecek veri boş.")

        command = """INSERT INTO {0}
                        (BookName,Author,ISBN) 
                        VALUES 
                        (?,?,?)""".format(self.table)

        self.cur.execute(command, (book.name, book.author, book.isbn))
        self.database.commit()

    def remove(self, id=int):

        if not self.connected:
            raise Exception("Veritabanı kapalı.")

        command = """DELETE FROM {0} where ID = {1}""".format(self.table, id)

        self.cur.execute(command)
        self.database.commit()

    def update(self, id, new_book=Book):
        if not self.connected:
            raise Exception("Veritabanı kapalı.")

        if new_book.is_empty():
            raise Exception("Güncellenecek veri boş.")

        command = """UPDATE {0} SET 
                        BookName = ?,
                        Author = ?,
                        ISBN = ?
          WHERE ID = ?""".format(self.table)
        self.cur.execute(
            command, (new_book.name, new_book.author, new_book.isbn, id))
        self.database.commit()
