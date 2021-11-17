## Importa a biblioteca Tkinter

from tkinter import *
from tkinter import font

## Importa a classe "registerNewOS" do arquivo "registerNewOS.py"

from registerNewOS import *

## Cria a classe da janela principal (inicial) do app

class mainWindow:
    
    ## Instancia o objeto mainWindow (classe da qual será a janela principal)

    def __init__(self, toplevel):

        ## Cria o atributo toplevel do Frame

        self.toplevel = toplevel

        ## Cria o Frame principal do Toplevel

        self.frameTitle = Frame(toplevel)
        self.frameTitle.pack()

        ## Cria a Label do título do app 

        self.labelTitle = Label(self.frameTitle, text="Ordens de Serviço (OS)", font = ('Arial Black', '20', 'bold'), pady = 20, padx = 100)
        self.labelTitle.pack()

        ## Cria a label onde os botões estarão inseridos

        self.labelButtons = Label(self.frameTitle)
        self.labelButtons.pack()

        ## Cria o botão de "Cadastrar nova OS"

        self.registerNewOSButton = Button(self.labelButtons, text="Cadastrar Nova OS", width = 30, height = 3, background = '#f51f1f', command = self.openOSRegistryWindow)
        self.registerNewOSButton.pack(side = LEFT, padx = 15, pady = 5)

        ## Cria o botão de "Procurar OS Existente"

        self.searchOSButton = Button(self.labelButtons, text="Procurar OS Existente", width = 30, height = 3, background = 'white')
        self.searchOSButton.pack(side = LEFT, padx = 15, pady = 5)

    ## Função responsável por abrir a nova janela de "Cadastrar nova OS"

    def openOSRegistryWindow(self):

        ## Cria um objeto Toplevel que sobrepõe as outras janelas

        self.newWindow = Toplevel(self.toplevel)

        ## Insere no objeto Toplevel a janela de "Cadastrar nova OS"

        self.app = registerNewOS(self.newWindow)

        ## Centraliza a janela "Cadastrar nova OS"

        centerWindow(self.newWindow)

def centerWindow(root):

    ## Mantém a tela root em constante atualização de tamanho

    root.update_idletasks()

    ## Captura a altura e largura do monitor

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    ## Captura a altura e largura do frame

    frameWidth = int(root.geometry().split('x')[0])
    frameHeight = int(root.geometry().split('x')[-1].split('+')[0])

    ## Calcula a posição (x,y) do frame centralizado 

    posX = (screenWidth / 2) - (frameWidth / 2)
    posY = (screenHeight / 2) - (frameHeight / 2)

    ## Aplica a posição (x,y) centralizada no frame

    root.geometry("%dx%d+%d+%d" %(frameWidth, frameHeight, posX, posY))

def main():

    ## Cria a instância de Tk (instância principal do Tkinter) e define seu título

    root = Tk()
    root.title("Ordens de Serviço")

    ## Cria a tela principal (Toplevel) da GUI do app

    mainWindow(root)

    ## Centraliza a tela Toplevel

    centerWindow(root)

    ## Comando para manter rodando a GUI

    root.mainloop()

if __name__ == '__main__':
    main()