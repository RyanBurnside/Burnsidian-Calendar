# This is a chore class, not very useful outside of my calendar
# This class attempts to bind the GUI to the Day_Data class

# TODO have the Chore class delete itself,  when button is pushed,
# currently it only deletes the GUI interface
# I deally it should mark itself as dead then run an external function to
# remove itself from the container it lives in.

from Tkinter import *
from day_data import *
from ScrolledText import ScrolledText

class Chore:
    def __init__(self, parent, day, day_index = None):
        # Create a new Chore object, loading day_index from Day
        # If day_index is not set, create blank Chore

        self.parent = parent
        self.frame = Frame(parent, borderwidth = 1, relief = RAISED)
        self.check =  Checkbutton(self.frame, text = "Done")
        self.check.pack(side = LEFT)
        self.text = ScrolledText(self.frame, wrap=WORD, width = 40, height = 3,
                                 selectbackground ="#ff5500")
        if(day_index != None):
            self.text.insert("1.0", day.get_index(day_index)[1])
        self.text.pack(side = LEFT)
        self.delete = Button(self.frame, width = 6,text = "Delete", command = 
                            lambda: self.frame.destroy()).pack(side = TOP)
        self.clear = Button(self.frame, width = 6, text = "Clear", command =
                            lambda: self.text.delete("1.0", END))
        self.clear.pack(side = BOTTOM)
        self.frame.pack()
