from tkinter import *
class MenuButtons:


    def __init__(self):
        # gui = Tk()
        test = 1
    def addNewItem(self, inventory):

        gui = Tk()

        print("add")
        gui.title("Add New Item(s)")
        gui.geometry("360x120")
        frame = Frame(gui, background="red")
        gridRow = 0
        fields = inventory.getFields("items", None)
        for field in fields:
            Label(frame, text = field, width = 10).grid(row = gridRow, column = 0)
            Entry(frame).grid(gridRow, column = 1)
            gridRow += 1
        gui.mainloop()

    def close(self):
        gui.close()
        del(self)
#
# myGUI = MainMenuButtons()
# myGUI.addNewItem()
