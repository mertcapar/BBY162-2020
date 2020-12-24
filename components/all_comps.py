from tkinter import Button, Menu, PhotoImage, Frame,TOP,X ,font
from tkinter.ttk import Treeview

class CustomButton(Button):
    def load(self,icon, coordinates = dict):
        fontw = font.Font(family='Segoe UI', size=10, weight='bold')

        self['font'] = fontw
        self.place(x=coordinates["x"], y=coordinates["y"], width=coordinates['w'], height = coordinates['h'])

        image = PhotoImage(file = icon)
        image = image.subsample(2)
        self.config(image=image, compound = 'left')
        self.image = image

    def n_pack(self, icon, packtype):
        fontw = font.Font(family='Segoe UI', size=10, weight='bold')

        self['font'] = fontw
        self.pack(side=packtype,padx = 1, pady = 0)

        image = PhotoImage(file=icon)
        self.config(image=image, compound='left')
        self.image = image

    def colorize(self, bg='#8F177D', fg='#97FF75', hbg='#97FF75', hfg='#8F177D'):
        self.config(bg=bg, fg=fg, activebackground=hbg,
                    highlightbackground=hfg)

class CustomToolbar(Frame):
    def load(self):
        self.pack(side = TOP, fill = X)

        fontw = font.Font(family='Segoe UI', size=10, weight='bold')

        add_btn = Button(self, text='Ekle', bg='#8F177D', fg='#97FF75', font = fontw, height = 2, command = self.master.add)
        add_btn.pack(side = 'left', padx = 1, pady = 0)

        update_btn = Button(self, text='Güncelle', bg='#8F177D',
                            fg='#97FF75', font = fontw, height = 2, command=self.master.update_value)
        update_btn.pack(side = 'left', padx = 1, pady = 0)
        
        delete_btn = Button(self, text='Sil', bg='#8F177D',
                            fg='#97FF75', font = fontw, height = 2, command=self.master.delete)
        delete_btn.pack(side = 'left', padx = 1, pady = 0)

        search_btn = Button(self, text='Ara', bg='#8F177D',
                            fg='#97FF75', font=fontw, height=2, command=self.master.search)
        search_btn.pack(side='left', padx=1, pady=0)

        close_db = Button(self, text='Kapat', bg='#8F177D',
                          fg='#97FF75', font = fontw, height = 2, command=self.master.close)
        close_db.pack(side='right', padx=1, pady=0)

        refresh_btn = Button(self, text='Listeyi Yenile',
                             bg='#8F177D', fg='#97FF75', font = fontw, height = 2, command=self.master.reload)
        refresh_btn.pack(side='right', padx=1, pady=0)

        self.config(bg='#3F8F25')


class CustomTree(Treeview):

    def load(self,datalist = []):
        self.reset()

        for i in datalist:
            self.add(i)

    def reset(self):
        self['columns'] = ('bookname', 'author', 'isbn')

        self.heading('#0', text='ID')
        self.column('#0', anchor='center', width=30)

        self.heading('bookname', text='Kitap Adı')
        self.column('bookname', anchor='center', width=100)

        self.heading('author', text='Yazar')
        self.column('author', anchor='center', width=100)

        self.heading('isbn', text='ISBN')
        self.column('isbn', anchor='center', width=100)
        self.pack(side = 'top', fill = 'both', expand = True,padx = 0, pady = 5)

        
    def add(self,data):
        
        self.insert('', 'end', data.id, text=data.id)
        self.set(data.id, 'bookname', data.name )
        self.set(data.id, 'author',data.author)
        self.set(data.id, 'isbn', data.isbn)

    def delete_selection(self):

        if self.selection() == '':
            raise Exception('Lütfen bir değer seçiniz.')
 
        id = int(self.selection()[0])
        self.delete(id)

    