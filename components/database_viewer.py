import tkinter as tk 
import components.all_comps as comps
import os,sqlite3
from components.modal import Modal
from components.database import SqlLiteConnection, Book

class Viewer(tk.Tk):

    def load(self, master, path, coords):

        self.resizable(0,0)
        self.ext_coords = coords
        self.geometry(f'800x600+{coords["x"] - 400}+{coords["y"] - 300}')
        
        self.config(bg='#3F8F25')
        self.title(os.path.basename(path) + ' - Veritabanı')

        self.protocol("WM_DELETE_WINDOW", self.close)

        self.master = master
        self.database = SqlLiteConnection(path)
        self.database.connect()
       
        tools = comps.CustomToolbar(self)
        tools.load()
        
        self.reload()

    def add(self):

        mod = Modal()
        mod.load(self, self.ext_coords)
        self.withdraw()
        mod.mainloop()

    def add_new(self,name,author,isbn):
        b = Book(-1,name,author,isbn)
        self.database.add(b)
        self.reload()
        
    def update_value(self):

        id = self.view.selection()[0]
        selected = self.view.item(id)['values']
        b = Book(id, selected[0], selected[1], selected[2])
        mod = Modal()
        mod.load_update(self,b,self.ext_coords)
        self.withdraw()
        mod.mainloop()

    def update_old(self,id,name,author,isbn):
        b = Book(id, name, author, isbn)
        self.database.update(id,b)
        self.reload()

    def delete(self):
        self.database.remove(int(self.view.selection()[0]))
        self.view.delete_selection()
        self.reload()


    def close(self):
        self.database.disconnect()
        self.master.deiconify()
        self.destroy()

    def reload(self):
        data_list = self.database.read_all()

        try:
            self.view.destroy()

        except:
            pass


        self.view = comps.CustomTree(self)
        self.view.load(data_list)

