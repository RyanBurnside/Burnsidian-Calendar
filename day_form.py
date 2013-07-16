import Tkinter
from ScrolledText import ScrolledText
import sys

# This widget looks for date data and loads it upong being called
# It also saves day data upon user clicking finish

class Day_Form(Tkinter.Frame):
    def __init__(self, parent, str_day, str_month, str_year, **options):
        self.my_frame = Tkinter.Frame.__init__(self, parent, **options)
        self.check_vars = [] # holds (BooleanVar()) 
        self.widgets = [] # holds (Checkbutton, ScrolledText)
        self.str_day = str_day
        self.str_month = str_month
        self.str_year = str_year

    def load_day(self, str_day, str_month, str_year):
        try:
            str_day = str(str_day)
            if len(str_day) == 1:
                str_day = '0' + str_day

            str_month = str(str_month)
            if len(str_month) == 1:
                str_month = '0' + str_month
 
            str_year = str(str_year)
            if len(str_year) != 4:
                print "Bad year value!"

            fname = str_year + str_month + str_day

            with open(fname, "r") as text_file:
                num_vals = int(text_file.readline().strip())
                for i in range(num_vals):
                    bb = Tkinter.BooleanVar()
                    self.check_vars.append(bb)

                    # Read value for check widget
                    truth = text_file.readline().strip()
                    if truth == "True":
                        self.check_vars[-1].set(1)
                    else:
                        self.check_vars[-1].set(0)

                    # Read value for ScrollText
                    chore = text_file.readline().strip()
                    temp_b = Tkinter.Checkbutton(self, 
                                         variable=self.check_vars[-1],
                                         text = "Done",
                                         onvalue = True, offvalue = False)
                    temp_t = ScrolledText(self,
                                          wrap=Tkinter.WORD, width = 40, height = 3,
                                          selectbackground ="#ff5500")
                    temp_t.insert("1.0",chore)
                    self.widgets.append([temp_b, temp_t])
                    self.widgets[-1][0].grid(row = i, column = 0)
                    self.widgets[-1][1].grid(row = i,column = 1)

        except Exception, e:
            exception_name, exception_value = sys.exc_info()[:2]
            raise
