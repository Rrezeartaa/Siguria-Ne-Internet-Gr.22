from sidebar import *
from display_pages import *

root = Tk()
root.resizable(False, False)
root.geometry("750x510")
main_frame = Frame(root, bg="grey", width=1000, height=1000)
main_frame.place(x=200, y=0)

sidebar = SideBar(root)
sidebar.add_spacer("LogFiles Application")
sidebar.add_button("Hyrje", lambda: HomePage(main_frame))
sidebar.add_button("Pjesa e testimit", lambda: TestingPage(main_frame))

sidebar.finish()

root.mainloop()
