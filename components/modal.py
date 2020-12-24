from tkinter import Tk, Button, Label, Entry, Frame , StringVar, font

class Modal(Tk):

    def load(self,master,coords):

        self.resizable(0, 0)
        self.geometry(f'400x200+{coords["x"] - 200}+{coords["y"] - 100}')
        self.config(bg='#3F8F25')
    
        self.title('Yeni girdi ekle')
        self.master = master

        fontw = font.Font(family='Segoe UI', size = 20, weight='bold')

        row1 = Frame(self, bg='#8F177D')
        label1 = Label(row1, width=15, font=fontw, text="Kitap Adı: ",
                       anchor='w', bg='#8F177D', fg='#97FF75')
        self.entry1 = Entry(row1,font = fontw)

        row2 = Frame(self, bg='#8F177D')
        label2 = Label(row2, width=15, text="Yazar: ", font = fontw,
                       anchor='w', bg='#8F177D', fg='#97FF75')
        self.entry2 = Entry(row2, font = fontw)

        row3 = Frame(self, bg='#8F177D')
        label3 = Label(row3, width=15,font = fontw,text="ISBN: ", anchor='w',bg='#8F177D' , fg='#97FF75')
        self.entry3 = Entry(row3,font = fontw)


        row1.pack(side='top', fill='x',  padx=5, pady=1)
        label1.pack(side='left')
        self.entry1.pack(side='right', expand=True, fill='x')

        row2.pack(side='top', fill='x', padx=5, pady=1)
        label2.pack(side='left')
        self.entry2.pack(side='right', expand=True, fill='x')

        row3.pack(side='top', fill='x',padx=5, pady=1)
        label3.pack(side='left')
        self.entry3.pack(side='right', expand=True, fill='x')

        frame = Frame(self)
        frame.pack(side='bottom', fill = 'x')
        frame.config(bg='#3F8F25')

        cancel_btn = Button(frame, text='Iptal', bg='#8F177D',
                        fg='#97FF75', font=fontw, height=2, width = 10, command = self.close)
        cancel_btn.pack(side='right', padx=1, pady=0)

        ok_btn  = Button(frame, text='Ekle',
                             bg='#8F177D', fg='#97FF75', font=fontw, height=2 ,width = 10, command= self.add_and_exit)
        ok_btn.pack(side='right', padx=1, pady=0)

        
        self.protocol("WM_DELETE_WINDOW", self.close)


    def load_update(self,master, book,coords):
        
        self.resizable(0, 0)
        self.geometry(f'400x200+{coords["x"] - 200}+{coords["y"] - 100}')
        self.config(bg='#3F8F25')
        
        self.title('Yeni girdi ekle')
        self.master = master

        self.exist_book = book  

        fontw = font.Font(family='Segoe UI', size=20, weight='bold')

      


        row1 = Frame(self, bg='#8F177D')
        label1 = Label(row1, width=15, font=fontw, text="Kitap Adı: ",
                       anchor='w', bg='#8F177D', fg='#97FF75')
        self.entry1 = Entry(row1,font=fontw)

        row2 = Frame(self, bg='#8F177D')
        label2 = Label(row2, width=15, text="Yazar: ", font=fontw,
                       anchor='w', bg='#8F177D', fg='#97FF75')
        self.entry2 = Entry(row2,font=fontw)

        row3 = Frame(self, bg='#8F177D')
        label3 = Label(row3, width=15, font=fontw, text="ISBN: ",
                       anchor='w', bg='#8F177D', fg='#97FF75')
        self.entry3 = Entry(row3,  font=fontw)

        row1.pack(side='top', fill='x',  padx=5, pady=1)
        label1.pack(side='left')
        self.entry1.pack(side='right', expand=True, fill='x')

        row2.pack(side='top', fill='x', padx=5, pady=1)
        label2.pack(side='left')
        self.entry2.pack(side='right', expand=True, fill='x')

        row3.pack(side='top', fill='x', padx=5, pady=1)
        label3.pack(side='left')
        self.entry3.pack(side='right', expand=True, fill='x')

        frame = Frame(self)
        frame.pack(side='bottom', fill='x')
        frame.config(bg='#3F8F25')


        self.entry1.delete(0,'end')
        self.entry1.insert(0,book.name)

        self.entry2.delete(0, 'end')
        self.entry2.insert(0, book.author)

        self.entry3.delete(0, 'end')
        self.entry3.insert(0, book.isbn)

        cancel_btn = Button(frame, text='Iptal', bg='#8F177D',
                            fg='#97FF75', font=fontw, height=2, width=10, command=self.close)
        cancel_btn.pack(side='right', padx=1, pady=0)

        ok_btn = Button(frame, text='Güncelle',
                        bg='#8F177D', fg='#97FF75', font=fontw, height=2, width=10, command=self.update_and_exit)
        ok_btn.pack(side='right', padx=1, pady=0)

        self.protocol("WM_DELETE_WINDOW", self.close)

    def add_and_exit(self):
        
        bookname = self.entry1.get()
        author = self.entry2.get()
        isbn = self.entry3.get()
        self.master.add_new(bookname, author, isbn)
        self.close()

    def update_and_exit(self):
        bookname = self.entry1.get()
        author = self.entry2.get()
        isbn = self.entry3.get()
        self.master.update_old(self.exist_book.id, bookname, author, isbn)
        self.close()

    def close(self):
        self.master.deiconify()
        self.destroy()
