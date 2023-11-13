import os
import shadeep as sd
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.font as font


class Application(tk.Tk):                                       # Application is a Tk Object
    def __init__(self) -> None:                                 
        super().__init__()                                      # Application inherits from Tk
        self.title("SHAdeep")                                   # Application Title
        self.geometry('1200x700')                               # root window size
        self.interface()                                        # Create Interface as ttk object
        #self.gen_tree()
      
    def interface(self):
    ### Notebook as TTK primary object#######################################################
        notebook=ttk.Notebook(self)
        tab1=ttk.Frame(notebook)
        tab2=ttk.Frame(notebook)
        notebook.add(tab1, text ='Tab 1')
        notebook.add(tab2, text ='Tab 2')
        notebook.pack(expand = 1, fill ="both")
        mypw1 = ttk.PanedWindow(tab1)
        #expand option for widgets to expand and fill for letting widgets adjust itself
        mypw1.pack(fill = tk.BOTH, expand = 1)
        # entry widget creation
        mye1 = ttk.Entry(mypw1, font = ('Calibri',12))
        # will add entry widget to the panedwindow
        mypw1.add(mye1)
        # 2nd paned window object
        mypw2 = ttk.PanedWindow(mypw1, orient = tk.VERTICAL)
        #adding 2nd paned window to the 1st paned window
        mypw1.add(mypw2)
        # spinbox object creation
        mye2 = ttk.Spinbox(mypw2, from_ = 10, to = 20, font = ('Calibri',12))
        # another entry widget creation
        mye3 = ttk.Entry(mypw2, font = ('Calibri',12) )
        #setting the value to 3
        mye3.insert(0,3)
        # to show sash
        mypw1.configure()
        # subtract function
        def subtract():
            num1 = int(mye2.get()) # getting value of spinbox
            num2 = int(mye3.get()) # getting value of entry
            mydata = str(num1-num2)
            mye1.insert(1,mydata)
        # adding spinbox to the 2nd paned window
        mypw2.add(mye2)
        # adding entry to the 2nd paned window
        mypw2.add(mye3)
        # creation of button widget
        mybtn = tk.Button(mypw2, text = "Subtract", command = subtract)
        # adding button to the 2nd paned window
        mypw2.add(mybtn)

    #### Place Widgets  ######################################################################
        """
        main_frame = ttk.Frame(self)
        notebook = ttk.Notebook(self)
        nb_1 = ttk.Frame(notebook)
        notebook.add(nb_1, text="Directory")
        tree_frame = ttk.Frame(nb_1, borderwidth=5, relief="ridge", width=200, height=100)
        self.tree_view = ttk.Treeview(tree_frame, selectmode='browse')
        self.tree_view.heading('#0', text='Name')
        self.tree_view.column('#0', stretch=False) # stretch needs to be "False" for hsb to work
        #self.tree_view.column('size', width=200)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree_view.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree_view.xview)
        self.tree_view.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_view.bind("<<TreeviewSelect>>", self.on_tree_select)
    #### Place Widgets  ######################################################################
        #main_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        notebook.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        tree_frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.tree_view.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        vsb.grid(column=1, row=0, sticky=(tk.N, tk.S))
        hsb.grid(column=0, row=1, sticky=(tk.E, tk.W))
        
    #### Configure for window resizing #######################################################
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #main_frame.columnconfigure(0, weight=1)
        #main_frame.rowconfigure(1, weight=1)
        notebook.columnconfigure(0, weight=1)
        notebook.rowconfigure(1, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
    
        """
    #### Generate Directory Tree #############################################################
    def gen_tree(self, path=os.getcwd()):
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
    #### JOIN PATH with text / SELECT MULTIPLE ENTRIES
####################
# Main Application #
####################

if __name__ == "__main__":      # if run from main program
    app = Application()           # Create App Object
    app.mainloop()                # Run mainloop
 