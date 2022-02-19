from hash import *
from tkinter import *


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
                
        self.password = Label(self.segundoContainer, text="Password")
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
        self.generator_hash["command"] = self.hash_generator
        self.generator_hash.pack(side = RIGHT)
        
    def hash_generator():
        h_password = hashes.hash_Password
        return h_password
    

root = Tk()
Application(root)
root.mainloop()
        
         

