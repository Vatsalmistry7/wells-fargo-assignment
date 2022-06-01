from tkinter import *

import pandas as pd


class Table:
    # Initialize a constructor
    def __init__(self, gui, df):
        total_rows, total_columns = df.shape
        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                if i == 0:
                    # initialize header
                    self.entry = Entry(gui, width=20, bg='LightSteelBlue', fg='Black',
                                       font=('Arial', 16, 'bold'))
                    self.entry.grid(row=i, column=j)
                    self.entry.insert(END, df.columns[j])
                else:
                    self.entry = Entry(gui, width=20, fg='blue',
                                       font=('Arial', 16, ''))

                    self.entry.grid(row=i, column=j)
                    self.entry.insert(END, df.values[i][j])


df = pd.read_csv("Output/consolidated_output_bonus.csv")
gui = Tk()
table = Table(gui, df)
gui.mainloop()
