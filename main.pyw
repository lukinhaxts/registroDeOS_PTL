from tkinter import *
from tkinter import font

from registerNewOS import *

class Janela:
    
    def __init__(self,toplevel):

        self.frameTitle = Frame(toplevel)
        self.frameTitle.pack()

        self.labelTitle = Label(self.frameTitle, text="Ordens de Serviço (OS)", font = ('Arial Black', '20', 'bold'), pady = 20, padx = 100)
        self.labelTitle.pack()

        self.labelButtons = Label(self.frameTitle)
        self.labelButtons.pack()

        self.registerNewOSButton = Button(self.labelButtons, text="Cadastrar Nova OS", width = 30, height = 3, background = '#f51f1f', command = self.openOSRegistryWindow)
        self.registerNewOSButton.pack(side = LEFT, padx = 15, pady = 5)

        self.searchOSButton = Button(self.labelButtons, text="Procurar por OS", width = 30, height = 3, background = 'white')
        self.searchOSButton.pack(side = LEFT, padx = 15, pady = 5)

        def openOSRegistryWindow(self):
            exec(open("./egisterNewOSButton.py").read())


raiz = Tk()
Janela(raiz)
raiz.mainloop()