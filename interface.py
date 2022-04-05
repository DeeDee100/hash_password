from tkinter import Tk, Label, Entry, Frame, Button, Toplevel, RIGHT, LEFT
import tkinter
import hashlib


class Application:
    def __init__(self, master=None):
        root.title("Gerador de Hashes")
        root.geometry("300x300")
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = "10"
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = "5"
        self.segundoContainer.pack()

        self.password = Label(self.segundoContainer, text="Password", height=5, width=0,
                              font=("Calibri", 20))
        self.password.pack(side=LEFT)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = "10"
        self.terceiroContainer.pack()

        self.txtpassword = Entry(self.terceiroContainer)
        self.txtpassword["width"] = 30
        self.txtpassword["font"] = self.fontePadrao
        self.txtpassword.pack(side=LEFT)

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 10
        self.quartoContainer.pack()

        self.generator_hash = Button(self.quartoContainer)
        self.generator_hash["text"] = "Gerar"
        self.generator_hash["font"] = self.fontePadrao
        self.generator_hash["width"] = 30
        self.generator_hash["command"] = self.hash_and_exhibt
        self.generator_hash.pack(side=RIGHT)

    def hash_and_exhibt(self):
        self.hash_Password()
        self.hashe_exbition()

    def hash_Password(self):
        pass_gen = self.txtpassword.get()
        hash_pass = hashlib.md5()
        text = pass_gen.encode("utf-8")
        hash_pass.update(text)
        return hash_pass.hexdigest()

    def hashe_exbition(self):
        new_window = Toplevel(root)
        new_window.title("Hashe Exibition")
        new_window.geometry("400x300")

        self.title_hash = tkinter.Label(new_window, text="Your Hash", font=(self.fontePadrao, 13), pady="100")
        self.HASHES = tkinter.Label(new_window, text=self.hash_Password(), font=(self.fontePadrao,14))
        self.HASHES.place(relx=0.5, rely=0.5, anchor='center')
        self.title_hash.pack()


root = Tk()
Application(root)
root.mainloop()
