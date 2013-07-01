# Day_Data class
# Stores a list of tupples (bool done, string "description")
# This class tries to load saved instances from previous sessions
# Bad form? Whatever. Gets the job done.

# TODO currently multi line strings for tasks will break the loader...

import os

class Day_Data(object):
    def __init__(self, day, month, year, save_dir):
        self.chores = []
        self.day = day
        self.month = month
        self.year = year
        # fname needs to be yyyymmdd
        self.fname = os.path.join(save_dir, year + month + day)
        self.load_data() # Tries to load self on instanciation

    def add_chore(self, bool_done, desc):
        self.chores.append([bool_done, desc])
            
    def delete_chore(self, index):
        del self.chores[index]

    def delete_chores(self):
        del self.chores[:]

    def get_index(self, index):
        return self.chores[index]

    def get_num_chores(self):
        return len(self.chores)

    def load_data(self):
        try:
            with open(self.fname, "r") as text_file:
                del self.chores[:] # Clear current list
                iter = int(text_file.readline())
                for i in range(iter):
                    done = bool(text_file.readline().strip())
                    chore = text_file.readline().strip()
                    self.add_chore(done, chore)
        except IOError:
            return
    
    def save_data(self):
        if len(self.chores): # If the object contains nothing, don't write
            with open(self.fname,"w") as text_file:
                text_file.write(str(len(self.chores)) + "\n")
                for i in self.chores:
                    print >> text_file, i[0]
                    print >> text_file, i[1]
  
