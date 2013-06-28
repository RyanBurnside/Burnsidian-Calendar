import day_data
from day_form import *
import calendar
import Tkinter
import datetime

# Global selection color
select_color = "#ff5500"

# Get the current date
today = datetime.date.today()

# This global lists holds the Dat_Data for the current month
cur_days = []

def make_cal (month, year):
    # Clear the old list of days, prepare to fill with new Day_Data objects
    del cur_days[:]

    # TODO clear all currently existing date buttons (will be container)

    # Get number of days to iterate over
    mrange = calendar.monthrange(int(year), int(month))

    first_day = mrange[0]

    # Lookup table for day English names
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
            "Thursday", "Friday", "Saturday"]

    # Account for bizzare Euroweek 
    if(first_day == 6):
        first_day = -1
    num_days = mrange[1]
    
    # Weekday labels
    for c in range(7):
        b = Tkinter.Label(root, text='%s'%(days[c]), borderwidth = 1)
        b.grid(row = 0, column = c)

    column = first_day + 1 # +1 for American offset 
    row = 1

    # Populate the grid with day buttons
    for r in range(num_days):
        # Fill list of Day_Data
        padded_day = str(r + 1)
        
        if (len(padded_day) == 1):
            padded_day = "0" + padded_day
        cur_days.append(Day_Data(padded_day, month, year,"Dates"))

        # Fill grid with buttons
        d = Tkinter.Button(root, text = '%s\n'%(r + 1),
                           borderwidth = 1, width = 6, height = 2, 
                           activebackground = select_color, 
                           command = lambda:messageWindow(root, cur_days[r]), 
                           bg = "#ffffff")

        if(int(today.strftime("%d")) == r + 1):
            d["text"] += "(Today)"

        d.grid(row=row,column=column)
        column += 1
        if(column > 6):
            row += 1;
            column = 0;

    Tkinter.Label(root, text = today.strftime("%x")).grid(row=num_days + 2, 
                                                          column = 0, 
                                                          columnspan = 6)

#--------TEST DATUM--------

#--------MAIN LOOP BEGIN--------
root = Tkinter.Tk()
root.title("Burnsidian Calendar Utility")

make_cal(today.strftime("%m"), today.strftime("%Y"))
root.mainloop()
