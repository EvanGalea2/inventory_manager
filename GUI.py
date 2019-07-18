from tkinter import *
from DatabaseConnector import *

global totalNumberOfItems
global totalCostOfItems
global totalValueOfItems
global useSQL #true if using the sql database
inventory = inventoryConnection("LocalHost","inventory","pythonScript","python")
screen = Tk()
screen.geometry("500x300")
screen.title("Inventory Manager")
mainText = StringVar()
mainDisplayText = Label()

#def updateMainDisplay():
def populate(frame, query):
    itemString = inventory.selectItems("items", query)
    gridRow = 1
    gridColumn = 0
    fields = inventory.getFields("items", None)
    for field in fields:
        Label(frame, text = field, width = 10).grid(row = gridRow - 1, column = gridColumn)
        gridColumn += 1
    gridColumn = 0
    for item in itemString:
        for var in item:
            Label(frame, text = var, width = 10).grid(row=gridRow, column=gridColumn)
            gridColumn += 1
        gridColumn = 0
        gridRow += 1
#buttons



def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))
canvas = Canvas(screen, borderwidth=0, background="#ffffff")

mainMenu = Frame(background="RED").pack(side="top")
fileButton = Button(mainMenu,text = "File", width = 10).pack(side = "top")
editButton = Button(mainMenu,text="Edit", width = 10).pack(side="top")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(screen, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="top", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))



populate(frame, None)

screen.mainloop()
