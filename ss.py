from sidebar import *
from display_pages import *

root = Tk()
root.resizable(False, False)
root.geometry("1300x500")
main_frame = Frame(root, bg="grey", width=1100, height=1000)
main_frame.place(x=200, y=0)

sidebar = SideBar(root)
sidebar.add_spacer("LogFiles Application")
sidebar.add_button("Hyrje", lambda: HomePage(main_frame))
sidebar.add_button("Pjesa e testimit", lambda: TestingPage(main_frame))

sidebar.finish()

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
                    
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=lambda:root.focus_get().event_generate('<<Undo>>') )
editmenu.add_command(label="Redo",accelerator="Ctrl+Y", command=lambda:root.focus_get().event_generate('<<Redo>>'))
editmenu.add_separator()

editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=lambda:root.focus_get().event_generate('<<Cut>>'))
editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=lambda:root.focus_get().event_generate('<<Copy>>'))

menubar.add_cascade(label="Edit", menu=editmenu)

root.mainloop()
