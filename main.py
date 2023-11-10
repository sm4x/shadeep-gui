import os
import shadeep as sd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font

SHASUMS = "sha256sums.txt"
current_dir=os.getcwd()

class Application(tk.Tk):                                       # Application is a Tk Object
    def __init__(self) -> None:                                 
        super().__init__()                                      # Application inherits from Tk
        self.title("SHAdeep")                                   # Application Title
        #self.geometry('1200x700')                               # root window size
        self.interface()                                        # Create Interface as ttk object
        #self.build_tree()
        
        
    def interface(self):
    #### Main Frame as TTK object##############################################################
        mf = ttk.Frame(self)
        frame = ttk.Frame(mf, borderwidth=5, relief="ridge", width=200, height=100)
        """self.tree  = ttk.Treeview(frame, 
                                      columns=self.tree_columns, 
                                      show="headings")"""
        
        
        
        namelbl = ttk.Label(mf, text="Name")
        name = ttk.Entry(mf)

        one = ttk.Checkbutton(mf, text="One", onvalue=True)
        two = ttk.Checkbutton(mf, text="Two", onvalue=True)
        three = ttk.Checkbutton(mf, text="Three", onvalue=True)
        ok = ttk.Button(mf, text="Okay")
        cancel = ttk.Button(mf, text="Cancel")

        mf.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        namelbl.grid(column=3, row=0, columnspan=2, sticky=(tk.N, tk.W), padx=5)
        name.grid(column=3, row=1, columnspan=2, sticky=(tk.N,tk.E,tk.W), pady=5, padx=5)
        one.grid(column=0, row=3)
        two.grid(column=1, row=3)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=3)
        cancel.grid(column=4, row=3)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        mf.columnconfigure(0, weight=3)
        mf.columnconfigure(1, weight=3)
        mf.columnconfigure(2, weight=3)
        mf.columnconfigure(3, weight=1)
        mf.columnconfigure(4, weight=1)
        mf.rowconfigure(1, weight=1)
    

    
####################
# Main Application #
####################

if __name__ == "__main__":      # if run from main program
  
  
    app = Application()           # Create App Object
    app.mainloop()                # Run mainloop
 