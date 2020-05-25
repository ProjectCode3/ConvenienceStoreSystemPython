from tkinter import Tk, Menu, Text
window = Tk()
menubar = Menu(window)
file_menu = Menu(menubar)
view_menu = Menu(menubar)
T = Text()


class Clients(object):
    def __init__(self, width, height, title, menu_bar, filemenu, viewmenu, text,  win, tear):
        self.width = width
        self.height = height
        self.title = title
        self.win = win
        self.menubar = menubar
        self.filemenu = filemenu
        self.viewmenu = viewmenu
        self.tear = 0
        self.text = text

    def getWidth(self):
        """
        returns the width of the frame
        :return: Int
        """
        return self.width

    def getHeight(self):
        """
        returns the height of the frame
        :return: Int
        """
        return self.height

    def getTitle(self):
        """
        return the title of the frame
        :return: Str
        """
        return self.title

    def draw(self):
        self.win.geometry(f"{self.width}x{self.height}")
        self.win.title(f"{self.getTitle()}")
        self.menubar = Menu(self.win)
        self.filemenu = Menu(self.menubar, tearoff=self.tear)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="New", command="")
        self.filemenu.add_command(label="Save", command="")
        self.filemenu.add_command(label="Save As", command="")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.win.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.viewmenu = Menu(self.menubar, tearoff=self.tear)
        self.viewmenu.add_command(label="Zoom In", command="")
        self.viewmenu.add_command(label="Zoom Out", command="")
        self.viewmenu.add_command(label="Show Time", command="")
        self.menubar.add_cascade(label="View", menu=self.viewmenu)

        self.text = Text(self.win, width=self.width, height=self.height)
        self.text.pack()

        self.win.config(menu=self.menubar)
        self.win.mainloop()


myClient = Clients(1280, 720, "Editor", menubar, file_menu, view_menu, T, window, 0)
myClient.draw()
