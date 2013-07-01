# This is a chore class, not very useful outside of my calendar


# TODO have the Chore class delete itself,  when button is pushed,
# currently it only deletes the GUI interface
# I deally it should mark itself as dead then run an external function to
# remove itself from the container it lives in.

# TODO currently the textarea is not filled with Day's chore upon creation.
# consider addint an optional index so the chore can get the text from the day

from Tkinter import *
from day_data import *
from ScrolledText import ScrolledText

class Chore:
    def __init__(self, parent, day):
        self.parent = parent
        self.frame = Frame(parent, borderwidth = 1, relief = RAISED)
        self.check =  Checkbutton(self.frame, text = "Done")
        self.check.pack(side = LEFT)
        self.text = ScrolledText(self.frame, width = 40, height = 3)
        self.text.pack(side = LEFT)
        self.delete =Button(self.frame, text = "Delete", command = 
                            lambda: self.frame.destroy()).pack(side = TOP)
        self.clear = Button(self.frame, text = "Clear", command =
               lambda: clear_text(self.frame)).pack(side = BOTTOM)
        self.frame.pack()

