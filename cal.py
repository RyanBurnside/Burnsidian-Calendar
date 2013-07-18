import calendar
import Tkinter
import datetime
from day_form import Day_Form


# Global selection color
select_color = "#ff5500"

# Get the current date
today = datetime.date.today()

# This global lists holds the Dat_Data for the current month
cur_days = []

# Global window 
root = Tkinter.Tk()
root.title("Burnsidian Calendar Utility")

# Day item list frame
my_form = Day_Form(root, today.strftime("%d"), today.strftime("%m"), 
                       today.strftime("%Y"), height =240, bd = 2, 
                       relief = Tkinter.SUNKEN)

def make_cal (month, year):
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
        # Fill grid with buttons
        d = Tkinter.Button(root, text = '%s\n'%(r + 1),
                           borderwidth = 1, width = 9, height = 2,
                           activebackground = select_color,
                           command = lambda r=r:
                           my_form.load_day(r + 1, month, year),
                           bg = "#ffffff")

        if(int(today.strftime("%d")) == r + 1):
            d["text"] += "(Today)"

        d.grid(row=row,column=column)
        column += 1
        if(column > 6):
            row += 1;
            column = 0;

    
    
    my_form.load_day(today.strftime("%d"), today.strftime("%m"), today.strftime("%Y"))
    my_form.grid(columnspan = 7, sticky = Tkinter.W + Tkinter.E + Tkinter.S)

#--------MAIN LOOP BEGIN--------
make_cal(today.strftime("%m"), today.strftime("%Y"))
root.mainloop()
