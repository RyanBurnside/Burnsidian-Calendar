# This is a chore class, not very useful outside of my calendar
# This class attempts to bind the GUI to the Day_Data class

from Tkinter import *
from day_data import *
from ScrolledText import ScrolledText

class Chore:
    def __init__(self, parent, day, day_index = None):
        # Create a new Chore object, loading day_index from Day
        # If day_index is not set, create blank Chore
        self.check_state = BooleanVar()
        #self.description = StringVar()
        self.this = self

        self.parent = parent
        self.frame = Frame(parent, borderwidth = 1, relief = RAISED)
                
        self.check = Checkbutton(self.frame, variable=self.check_state, 
                                 text = "Done",
                                 onvalue = True, offvalue = False)
        
        self.textb = ScrolledText(self.frame, 
                                 wrap=WORD, width = 40, height = 3,
                                 selectbackground ="#ff5500")
        
        if(day_index != None):
            self.textb.insert("1.0", day.get_index(day_index)[1])
            self.check_state.set(day.get_index(day_index)[0])
        
            print day.get_index(day_index)[0].__class__
        else:
            self.check_state.set(0)

            
        self.check.pack(side = LEFT)
        self.textb.pack(side = LEFT)
        self.delete = Button(self.frame, width = 6,text = "Delete", command = 
                            lambda: self.seppuku()).pack(side = TOP)
        self.clear = Button(self.frame, width = 6, text = "Clear", command =
                            lambda: self.text.delete("1.0", END))
        self.clear.pack(side = BOTTOM)
        self.frame.pack()

    def seppuku(self):
        # Really bad design here, instances should not delete themselves...
        self.frame.destroy()
        del self

