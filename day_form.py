import Tkinter
from ScrolledText import ScrolledText
import sys

# Constant for file specification version
FILE_VERSION = 1.0

# This widget looks for date data and loads it upong being called
# It also saves day data upon user clicking finish

class Day_Form(Tkinter.Frame):
    def __init__(self, parent, str_day, str_month, str_year, **options):
        self.my_frame = Tkinter.Frame.__init__(self, parent, **options)
        self.item_frame = Tkinter.Frame(self)
        self.check_vars = [] # holds (BooleanVar())
        self.widgets = [] # holds (Checkbutton, ScrolledText)
        self.str_day = str_day
        self.str_month = str_month
        self.str_year = str_year
        self.confirm = Tkinter.Button(self, text = "Save")
        self.refresh = Tkinter.Button(self, text = "Revert")             
        self.add = Tkinter.Button(self, text = "Add Item")             

    def load_day(self, str_day, str_month, str_year):
        # TODO dump all containers before loading new day
        # Break out function to load items so the GUI buttons don't get
        # recreated with each call to load_day
        self.confirm.destroy()
        self.refresh.destroy()
        self.add.destroy()
        self.item_frame.destroy() #kill old one with big size
        self.item_frame = Tkinter.Frame(self) # Start fresh
        del self.check_vars[:]

        for i in self.widgets:
            i[0].destroy()
            i[1].frame.destroy()
            i[1].destroy()
        del self.widgets[:]

        # Call delete on all widgets prior to dumping containers
        try:
            self.str_day = str(str_day)
            if len(self.str_day) == 1:
                self.str_day = '0' + str_day

            self.str_month = str(str_month)
            if len(self.str_month) == 1:
                self.str_month = '0' + str_month
 
            self.str_year = str(str_year)
            if len(self.str_year) != 4:
                print "Bad year value!"

            fname = self.str_year + self.str_month + self.str_day

            with open(fname, "r") as text_file:
                
                file_ver = float(text_file.readline().strip())
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
                    temp_b = Tkinter.Checkbutton(self.item_frame,
                                         variable=self.check_vars[-1],
                                         text = "Done",
                                         onvalue = True, offvalue = False)
                    temp_t = ScrolledText(self.item_frame,
                                          wrap=Tkinter.WORD,
                                          height = 2,
                                          selectbackground ="#ff5500")
                    temp_t.insert("1.0",chore.replace('\\n', '\n'))

                    self.widgets.append([temp_b, temp_t])
                    self.widgets[-1][0].pack(anchor = Tkinter.W)
                    self.widgets[-1][1].pack(side = Tkinter.TOP) 
        

        except Exception, e:
            pass
        
        self.item_frame.grid(row = 0, columnspan = 7)                                             
        self.confirm = Tkinter.Button(self, text = "Save",
                                      command = lambda:
                                          self.save_day())
        self.confirm.grid(row = len(self.widgets) + 1, column = 0)

        self.refresh = Tkinter.Button(self, text = "Revert",
                                      command = lambda:
                                          self.load_day(self.str_day, 
                                                        self.str_month,
                                                        self.str_year))
        self.refresh.grid(row = len(self.widgets) + 1, column = 1)

        self.add = Tkinter.Button(self, text = "Add Item",
                                  command = lambda:
                                      self.add_new_item())
        self.add.grid(row = len(self.widgets) + 1, column = 2)

    def save_day(self):
        # Save the contents of the GUI and quits
        fname = self.str_year + self.str_month + self.str_day
        with open(fname, "w") as text_file:
            text_file.write(str(FILE_VERSION) + '\n')
            text_file.write(str(len(self.widgets)) + '\n')
            for i in range(len(self.widgets)):
                if(self.check_vars[i].get() == 1):
                    text_file.write("True\n")
                else:
                    text_file.write("False\n")
                text_file.write(str(self.widgets[i][1].get('1.0', Tkinter.END)).strip().replace('\n',"\\n") + '\n')

    def add_new_item(self):
        bb = Tkinter.BooleanVar()
        self.check_vars.append(bb)

        self.check_vars[-1].set(0)
        
        # Read value for ScrollText
        chore = ""
        temp_b = Tkinter.Checkbutton(self.item_frame,
                                     variable=self.check_vars[-1],
                                     text = "Done",
                                     onvalue = True, offvalue = False)
        temp_t = ScrolledText(self.item_frame,
                              wrap=Tkinter.WORD,
                              height = 2,
                              selectbackground ="#ff5500")
        temp_t.insert("1.0","")
        self.widgets.append([temp_b, temp_t])
        self.widgets[-1][0].pack(anchor = Tkinter.W) 
        self.widgets[-1][1].pack(side = Tkinter.TOP) 

                           

