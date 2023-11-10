import os
import shadeep as sd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font


class Application(tk.Tk):                                       # Application is a Tk Object
    def __init__(self) -> None:                                 
        super().__init__()                                      # Application inherits from Tk
        self.title("SHAdeep")                                   # Application Title
        self.geometry('1200x700')                               # root window size
        self.interface()                                        # Create Interface as ttk object
  
      
    def interface(self):
    #### Main Frame as TTK object##############################################################
        main_frame = ttk.Frame(self)
        tree_frame = ttk.Frame(main_frame, borderwidth=5, relief="ridge", width=200, height=100)
        self.tree_view = ttk.Treeview(tree_frame)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree_view.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree_view.xview)
        self.tree_view.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
    #### Place Widgets  ########################################################################
        main_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        tree_frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.tree_view.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        vsb.grid(column=1, row=0, sticky=(tk.N, tk.S))
        hsb.grid(column=0, row=1, sticky=(tk.E, tk.W))
        
    #### Configure for window resizing ########################################################
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
    
####################
# Main Application #
####################

if __name__ == "__main__":      # if run from main program
    app = Application()           # Create App Object
    app.mainloop()                # Run mainloop
 