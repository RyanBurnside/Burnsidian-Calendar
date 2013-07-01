# This is a tkinter form to collect day data

from Tkinter import *
from day_data import *
from ScrolledText import ScrolledText
from chore import *

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


def add_chore(chore_list, contain_frame, day):
    chore_list.append(Chore(contain_frame, day))

def populate_chores(chore_list, contain_frame, day, iterator): 
    add_chore(chore_list, contain_frame, day)
    if(day.get_index(iterator)[0]):
        chore_list[-1].check.select()

    
def messageWindow(parent, day):
    # define list to hold chores
    my_chores = []

    # Create child window
    message_window = Toplevel()
    message_window.title(day.month + "/" + day.day + "/" + day.year + "  M/D/Y")
    num_lines = day.get_num_chores()
    main_frame = Frame(message_window, width = 320, height = 240)
    chores_frames_frame = Frame(main_frame)

    for i in range(num_lines):
        populate_chores(my_chores, chores_frames_frame, day, i)
    
    chores_frames_frame.pack()
    main_frame.pack()
    ff = Frame(main_frame)
    Button(ff, text = "Add Item",
           command = lambda:
               add_chore(my_chores, chores_frames_frame, day)).pack(side = TOP)
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
