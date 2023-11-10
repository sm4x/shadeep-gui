import os
import shadeep as sd
import tkinter as tk
import tkinter.ttk as ttk

SHASUMS = "sha256sums.txt"
current_dir=os.getcwd()

class Application(tk.Tk):                                       # Application is a Tk Object
    def __init__(self) -> None:                                 
        super().__init__()                                      # Application inherits from Tk
        self.title("SHAdeep")                                   # Application Title
        self.geometry('1200x700')                               # root window size
        self.columnconfigure(0, weight=1)                       # configure root windo grid to
        self.rowconfigure(0, weight=1)                          # use whitespace when resizing
        self.interface()                                        # Create Interface as ttk object
        
    def interface(self):
    #### Main Frame as TTK object##############################################################
        mf = ttk.Frame(self, borderwidth=5, relief="ridge",)                                    
        mf.grid(column=0, 
                row=0, 
                sticky=(tk.N, tk.W, tk.E, tk.S))                # frame is sticky to the rootwindow edges
        
    #### TreeView with frame #################################################################        
        tree_columns = ("1", "2", "3")
        tree_frame = ttk.Frame(mf,                              # Frame containing directory listing tree
                               borderwidth=15,
                               relief="ridge",)
                               #width=200,                      # DEBUG
                               #height=100)                     # DEBUG
        tree_frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S)) 
        tree_view = ttk.Treeview(tree_frame, columns=tree_columns, show="headings")
        tree_view.pack(fill='both', expand=True)                # Using simple packing for only widget in frame                
        
        """ Boilerplate code from https://tkdocs.com/tutorial/grid.html  
        namelbl = ttk.Label(mf, text="Name")
        name = ttk.Entry(mf)
        onevar = tk.BooleanVar(value=True)
        twovar = tk.BooleanVar(value=False)
        threevar = tk.BooleanVar(value=True)
        one = ttk.Checkbutton(mf, text="One", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(mf, text="Two", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(mf, text="Three", variable=threevar, onvalue=True)
        ok = ttk.Button(mf, text="Okay")
        cancel = ttk.Button(mf, text="Cancel")
        mf.grid(column=0, row=0)
        frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        namelbl.grid(column=3, row=0, columnspan=2)
        name.grid(column=3, row=1, columnspan=2)
        one.grid(column=0, row=3)
        two.grid(column=1, row=3)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=3)
        cancel.grid(column=4, row=3)
        """
        for i in (range(5)):
            mf.columnconfigure(i, weight=1)                       # use whitespace when resizing
            mf.rowconfigure(i, weight=1)
        for child in mf.winfo_children():
            print(child)

    
         
    #def quit_button(self) -> None:
    #    self.quit_button = ttk.Button(self,                     # Quit Button on main level
    #                                 text='Quit', 
    #                                 command=self.quit)
    #    self.quit_button.pack(padx=50, pady=5)                  # Main Level using pack manager
        
    
####################
# Main Application #
####################

if __name__ == "__main__":      # if run from main program
  
  
    app = Application()           # Create App Object
    app.mainloop()                # Run mainloop
 