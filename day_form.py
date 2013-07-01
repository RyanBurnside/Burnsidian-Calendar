# This is a tkinter form to collect day data

from Tkinter import *
from day_data import *
from ScrolledText import ScrolledText

def save_changes(day):
    # TODO function not implimented yet...

    # Clear all chores
    day.delete_chores();

    # Repopulate day's list with items from text fields

def clear_text(chore_frame):
    # TODO remove this silly iteration and create a composite widget for chores
    # Find textbox in chore_frame and set text to ""
    # Iterate through children of children to find the darn Text widget
    for i in chore_frame.winfo_children():  
        if i.winfo_class() == "Frame":
            for j in i.winfo_children():
                if j.winfo_class() == "Text":
                    j.delete("1.0", END)
                    return 

def populate_chores(contain_frame, day, iterator): 
    # Uses an external iterator to fill out the GUI
    # At some point this should be merged with add_chore() below
    f = Frame(contain_frame, borderwidth = 1, relief = RAISED)
    b =  Checkbutton(f, text = "Done")
    if(day.get_index(iterator)[0]):
        b.select()
    b.pack(side = LEFT)
    e = ScrolledText(f, width = 40, height = 3)
    e.insert("1.0", day.get_index(iterator)[1])
    e.pack(side = LEFT)
    Button(f, text = "Delete", command = 
           lambda: f.destroy()).pack(side = TOP)
    Button(f, text = "Clear", command =
           lambda: clear_text(f)).pack(side = BOTTOM)
    f.pack()

def add_chore(contain_frame, day):
    f = Frame(contain_frame, borderwidth = 1, relief = RAISED)
    b =  Checkbutton(f, text = "Done")
    b.pack(side = LEFT)
    e = ScrolledText(f, width = 40, height = 3)
    e.pack(side = LEFT)
    Button(f, text = "Delete", command = 
           lambda: f.destroy()).pack(side = TOP)
    Button(f, text = "Clear", command =
           lambda: clear_text(f)).pack(side = BOTTOM)
    f.pack()


def messageWindow(parent, day):
    # Create child window
    message_window = Toplevel()
    message_window.title(day.month + "/" + day.day + "/" + day.year + "  M/D/Y")
    num_lines = day.get_num_chores()
    main_frame = Frame(message_window, width = 320, height = 240)
    chores_frames_frame = Frame(main_frame)

    for i in range(num_lines):
        populate_chores(chores_frames_frame, day, i)
    
    chores_frames_frame.pack()
    main_frame.pack()
    ff = Frame(main_frame)
    Button(ff, text = "Add Item",
           command = lambda:
               add_chore(chores_frames_frame, day)).pack(side = TOP)
    Button(ff, text = "Finish",
           command = lambda: 
               message_window.destroy()).pack(side = LEFT)
    Button(ff, text = "Cancel",
           command = lambda: 
               message_window.destroy()).pack(side = RIGHT)
    ff.pack()
    x = parent.winfo_x() + 32
    y = parent.winfo_y() + 32

    message_window.geometry("+%d+%d" % (x, y))
