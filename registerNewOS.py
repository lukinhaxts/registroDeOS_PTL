from tkinter import *
from tkinter import font

class Janela:
    
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()