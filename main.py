import os
from pathlib import Path
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
        self.gen_tree()
      
    def interface(self):
    #### Main Frame as TTK object#############################################################
        main_frame = ttk.Frame(self)
        tree_frame = ttk.Frame(main_frame, borderwidth=5, relief="ridge", width=200, height=100)
        self.tree_view = ttk.Treeview(tree_frame, selectmode='browse')
        self.tree_view.heading('#0', text='Name')
        self.tree_view.column('#0', stretch=False) # stretch needs to be "False" for hsb to work
        #self.tree_view.column('size', width=200)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree_view.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree_view.xview)
        self.tree_view.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_view.bind("<<TreeviewSelect>>", self.on_tree_select)
    #### Place Widgets  ######################################################################
        main_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        tree_frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.tree_view.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        vsb.grid(column=1, row=0, sticky=(tk.N, tk.S))
        hsb.grid(column=0, row=1, sticky=(tk.E, tk.W))
        
    #### Configure for window resizing #######################################################
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
    
    
    #### Generate Directory Tree #############################################################
    def gen_tree(self, path=os.getcwd()):
        path="/usr"
        directories =[os.path.relpath(x[0],os.path.dirname(path)) for x in os.walk(path)]
        directories.sort()
        for directory in directories:
            parent = str(os.path.dirname(directory))
            #print(directory, ", ", parent)
            self.tree_view.insert(parent, 'end', iid=str(directory), text=str(directory))
            
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "text")
            print(item_text)
    #### JOIN PATH with text
####################
# Main Application #
####################

if __name__ == "__main__":      # if run from main program
    app = Application()           # Create App Object
    app.mainloop()                # Run mainloop
 