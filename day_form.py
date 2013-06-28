# This is a tkinter form to collect day data
from Tkinter import *
from day_data import *

def messageWindow(parent, day):
    # create child window
    win = Toplevel()
    win.title("TODO For ")
    num_lines = day.get_num_chores()
    main_frame = Frame(win, width = 320, height = 240)
    #canvas=Canvas(main_frame, width = 320, height = 240)
    #scroll_bar = Scrollbar(main_frame, orient = VERTICAL)
    #scroll_bar.pack(side = RIGHT, fill = Y)
    #scroll_bar.config(command=canvas.yview)
    #canvas.config(width = 300, height = 240)
    #canvas.config(yscrollcommand=scroll_bar.set)
    print num_lines

    for i in range(num_lines):
        f = Frame(main_frame)
        b =  Checkbutton(f)
        if(day.get_index(i)[0]):
            b.select()
        b.pack(side = LEFT)
        e = Text(f, width = 40, height = 3)
        e.insert("1.0", day.get_index(i)[1])
        e.pack(side = LEFT)
        Button(f, text = "Delete").pack(side = LEFT)
        f.pack()

    
    #canvas.config(scrollregion = (0,0, 320,200))
    #canvas.pack(side = LEFT, expand = TRUE, fill = BOTH)
    main_frame.pack()

    x = parent.winfo_x() + 32
    y = parent.winfo_y() + 32

    win.geometry("+%d+%d" % (x, y))

    
