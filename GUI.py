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
def populate(frame):
    '''Put in some fake data'''
    for row in range(100):
        Label(frame, text="%s" % row, width=3, borderwidth="1",
                 relief="solid").grid(row=row, column=0)
        t="this is the second column for row %s" %row
        Label(frame, text=t).grid(row=row, column=1)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(screen, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(screen, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

screen.mainloop()

itemString = inventory.selectItems("items", None)
print(type(itemString))
#itemString = itemString[1:-1]#cut out the first and last character in the string
#print(itemString)
for i in itemString:
    print(i)
    print(type(i))
